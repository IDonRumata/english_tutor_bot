#!/bin/bash
set -e

echo "=== English Tutor Bot Setup ==="

cd /root/english_tutor_bot

# Python venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Data dirs
mkdir -p data/english/tts_cache
mkdir -p data/english/sources

# Copy PDFs from old bot if they exist
if [ -f /root/andrey_agent/data/english/sources/sb.pdf ]; then
    cp /root/andrey_agent/data/english/sources/sb.pdf data/english/sources/
    cp /root/andrey_agent/data/english/sources/wb.pdf data/english/sources/ 2>/dev/null || true
    echo "PDFs copied from old bot"
fi

# Copy existing DB if present
if [ -f /root/andrey_agent/data/english.db ]; then
    cp /root/andrey_agent/data/english.db data/english.db
    echo "DB copied from old bot"
fi

# Copy TTS cache if present
if [ -d /root/andrey_agent/data/english/tts_cache ]; then
    cp -r /root/andrey_agent/data/english/tts_cache/. data/english/tts_cache/
    echo "TTS cache copied"
fi

# .env from template
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env — edit it and add your tokens!"
fi

# Systemd service
cp deploy/english-tutor.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable english-tutor

echo ""
echo "=== Setup complete ==="
echo "1. Edit /root/english_tutor_bot/.env — add ENGLISH_BOT_TOKEN"
echo "2. systemctl start english-tutor"
echo "3. systemctl status english-tutor"
