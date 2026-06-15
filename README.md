# English Tutor Bot

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Educational%20Bot-0088cc?logo=telegram)](https://core.telegram.org/bots/api)
[![Claude AI](https://img.shields.io/badge/Claude-Language%20Teacher-D97757?logo=anthropic&logoColor=white)](https://www.anthropic.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**English Tutor Bot** — интерактивный Telegram репетитор английского на основе Claude AI. Проводит уроки, исправляет ошибки в реальном времени, отслеживает прогресс и адаптирует сложность под уровень ученика.

**Целевая аудитория:** Изучающие английский (beginner → intermediate)  
**Язык интерфейса:** Russian (русский)  
**Стоимость:** Free / Pro подписка

---

## ✨ Ключевые возможности

| Функция | Описание |
|---------|---------|
| 📚 **Интерактивные уроки** | Грамматика, словарь, разговорная речь — по твоему уровню |
| ✍️ **Проверка грамматики** | Claude исправляет ошибки и объясняет почему |
| 🗣️ **Произношение** | Фонетический разбор слов |
| 📈 **Прогресс & Статистика** | Отслеживание уровня, время учёбы, процент правильных ответов |
| 🎯 **Адаптивность** | Сложность уроков растёт с твоим уровнем |
| 💬 **Диалоги** | Тренировка разговорных навыков через сценарии |
| 📝 **Домашние задания** | ДЗ с автоматической проверкой |

---

## 🏗️ Архитектура

```
┌──────────────────────────────────────────┐
│ User Message (Telegram)                  │
└──────────────┬───────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│ Router (Lesson Type Detection)           │
│ • Grammar → /grammar                     │
│ • Vocabulary → /vocabulary               │
│ • Conversation → /talk                   │
│ • Homework check → /check                │
└──────────────┬───────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│ Claude API (Lesson Generation)           │
│ • Lesson prompt (custom per type)        │
│ • User level (A1–B2)                     │
│ • Context (progress history)             │
└──────────────┬───────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│ Response + Feedback                      │
│ • Lesson content                         │
│ • Explanation (if grammar correction)    │
│ • Progress update → PostgreSQL            │
└──────────────────────────────────────────┘
```

---

## 🛠️ Стек технологий

- Python 3.11+ (aiogram 3.x)
- PostgreSQL (user profiles, progress, lessons history)
- Anthropic Claude (lesson generation, corrections)
- Docker

---

## 🚀 Быстрый старт

```bash
git clone https://github.com/IDonRumata/english_tutor_bot.git
cd english_tutor_bot

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Заполни TELEGRAM_BOT_TOKEN, ANTHROPIC_API_KEY, DATABASE_URL

python bot.py
```

---

## 🤖 Команды

| Команда | Описание |
|---|---|
| `/start` | Начало, выбор уровня |
| `/lesson` | Новый урок (автоматический выбор темы) |
| `/grammar` | Урок грамматики |
| `/vocabulary` | Новые слова |
| `/talk` | Разговорная практика |
| `/check` | Проверить написанное |
| `/progress` | Мой прогресс |
| `/level` | Изменить уровень сложности |

---

## 📊 Уровни

- **A1:** Absolute Beginner (основные фразы)
- **A2:** Elementary (базовые навыки)
- **B1:** Intermediate (свободное общение)
- **B2:** Upper-Intermediate (продвинутый)

Бот автоматически поднимает уровень после 20+ правильных ответов.

---

## 💡 Примеры

### Урок грамматики (Present Simple)

```
Бот: Let's learn Present Simple! 
     Choose: A) I go to school daily
             B) I going to school daily
             
Юзер: A

Бот: ✅ Correct! We use Present Simple for habits.
     Rule: Subject + Base Verb (3rd person + s)
     
     Your turn: "She _____ (to study) English"
     
Юзер: She studies English

Бот: ✅ Perfect! You completed this lesson.
     Progress: Grammar 85% → 90%
```

### Проверка текста

```
Юзер: He go to work yesterday

Бот: ❌ Error found!
     "He go" → "He went" (Past Simple needed)
     
     Why? We use Past Simple for actions in the past.
     Regular verbs add -ed, but "go" is irregular → "went"
     
     Corrected: "He went to work yesterday"
```

---

## 📈 Бизнес-модель

```
FREE: 5 lessons/день
PRO: Unlimited lessons ($4.99/месяц)

Target: 1000 FREE users → 50 PRO = $250/месяц
        5000 FREE → 250 PRO = $1,250/месяц
```

---

## 📞 Контакты

- **Telegram:** [@DonRumataE](https://t.me/DonRumataE)

---

*Учи английский как с репетитором, но 24/7 и за копейки.*
