"""English Tutor Bot — точка входа."""
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

import config
from fsm_storage import SQLiteFSMStorage
from handlers import english
import database as db


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger(__name__)

    await db.init_db()

    bot = Bot(token=config.TELEGRAM_TOKEN)
    storage = SQLiteFSMStorage(config.FSM_DB_PATH)
    dp = Dispatcher(storage=storage)
    dp.include_router(english.router)

    await bot.set_my_commands([
        BotCommand(command="en", description="Главное меню"),
        BotCommand(command="en_start", description="Placement test (оценка уровня)"),
        BotCommand(command="en_block", description="Блок упражнений (~10 мин)"),
        BotCommand(command="en_review", description="Повторение (SRS)"),
        BotCommand(command="en_speak", description="Speaking practice"),
        BotCommand(command="en_lesson", description="Отчёт с живого урока"),
        BotCommand(command="en_unit", description="Установить текущий юнит"),
        BotCommand(command="en_progress", description="Мой прогресс"),
        BotCommand(command="en_voice", description="Сменить голос TTS"),
        BotCommand(command="en_homework", description="Мои ДЗ"),
        BotCommand(command="skip", description="Пропустить упражнение"),
    ])

    logger.info("English Tutor Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
