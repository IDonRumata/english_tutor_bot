"""English Tutor Bot — конфигурация."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

TELEGRAM_TOKEN = os.getenv("ENGLISH_BOT_TOKEN", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# База данных
DB_PATH = Path(os.getenv("EN_DB_PATH", "data/english.db"))
FSM_DB_PATH = Path(os.getenv("EN_FSM_DB_PATH", "data/fsm.db"))

# Контент
EN_DATA_DIR = Path(os.getenv("EN_DATA_DIR", "data/english"))
EN_AUDIO_DIR = Path(os.getenv("EN_AUDIO_DIR", "data/english/tts_cache"))
EN_TTS_CACHE_DIR = Path(os.getenv("EN_TTS_CACHE_DIR", "data/english/tts_cache"))
EN_OUTCOMES_SB_PDF = os.getenv("EN_OUTCOMES_SB_PDF", "data/english/sources/sb.pdf")
EN_OUTCOMES_WB_PDF = os.getenv("EN_OUTCOMES_WB_PDF", "data/english/sources/wb.pdf")

# Создать директории при импорте
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
EN_DATA_DIR.mkdir(parents=True, exist_ok=True)
EN_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
EN_TTS_CACHE_DIR.mkdir(parents=True, exist_ok=True)

# TTS
EN_TTS_VOICE_MAIN = os.getenv("EN_TTS_VOICE_MAIN", "en-GB-SoniaNeural")
EN_TTS_VOICE_SECOND = os.getenv("EN_TTS_VOICE_SECOND", "en-GB-RyanNeural")
EN_TTS_RATE = os.getenv("EN_TTS_RATE", "-5%")
EN_TTS_PROVIDER = os.getenv("EN_TTS_PROVIDER", "edge")

# Whisper
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "whisper-1")
WHISPER_MIN_DURATION_SEC = int(os.getenv("WHISPER_MIN_DURATION_SEC", "2"))

# Claude
CLAUDE_MAX_TOKENS = int(os.getenv("CLAUDE_MAX_TOKENS", "1000"))
CHAT_HISTORY_LIMIT = int(os.getenv("CHAT_HISTORY_LIMIT", "0"))  # 0 = no history for tutor
