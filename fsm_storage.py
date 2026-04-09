"""
SQLite-based FSM storage for aiogram 3.
Persists FSM states across bot restarts — fixes context loss on restart.
"""
import json
import logging
from typing import Any

import aiosqlite
from aiogram.fsm.storage.base import BaseStorage, StorageKey, StateType

logger = logging.getLogger(__name__)


class SQLiteFSMStorage(BaseStorage):
    def __init__(self, db_path: str):
        self._db_path = db_path
        self._db: aiosqlite.Connection | None = None

    async def _get_db(self) -> aiosqlite.Connection:
        if self._db is None:
            self._db = await aiosqlite.connect(self._db_path)
            await self._db.execute("""
                CREATE TABLE IF NOT EXISTS fsm_states (
                    key TEXT PRIMARY KEY,
                    state TEXT,
                    data TEXT DEFAULT '{}'
                )
            """)
            await self._db.commit()
        return self._db

    def _key(self, key: StorageKey) -> str:
        return f"{key.bot_id}:{key.chat_id}:{key.user_id}"

    async def set_state(self, key: StorageKey, state: StateType = None) -> None:
        db = await self._get_db()
        state_str = state.state if hasattr(state, "state") else (str(state) if state else None)
        k = self._key(key)
        await db.execute("""
            INSERT INTO fsm_states (key, state, data) VALUES (?, ?, '{}')
            ON CONFLICT(key) DO UPDATE SET state=excluded.state
        """, (k, state_str))
        await db.commit()

    async def get_state(self, key: StorageKey) -> str | None:
        db = await self._get_db()
        async with db.execute("SELECT state FROM fsm_states WHERE key=?", (self._key(key),)) as cur:
            row = await cur.fetchone()
        return row[0] if row else None

    async def set_data(self, key: StorageKey, data: dict[str, Any]) -> None:
        db = await self._get_db()
        k = self._key(key)
        await db.execute("""
            INSERT INTO fsm_states (key, state, data) VALUES (?, NULL, ?)
            ON CONFLICT(key) DO UPDATE SET data=excluded.data
        """, (k, json.dumps(data, ensure_ascii=False)))
        await db.commit()

    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        db = await self._get_db()
        async with db.execute("SELECT data FROM fsm_states WHERE key=?", (self._key(key),)) as cur:
            row = await cur.fetchone()
        if not row or not row[0]:
            return {}
        try:
            return json.loads(row[0])
        except Exception:
            return {}

    async def close(self) -> None:
        if self._db:
            await self._db.close()
            self._db = None
