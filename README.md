# 💰 Expense Tracker Bot

Telegram-бот для учета расходов.

Бот позволяет добавлять расходы, хранить историю операций и быстро получать информацию о тратах прямо в Telegram.

## 🚀 Возможности

- Добавление расходов
- Просмотр последних операций
- Хранение данных в SQLite
- Работа 24/7 на VPS сервере
- Быстрый доступ к истории расходов

## 🛠 Технологии

- Python 3.12
- Aiogram 3.x
- SQLite
- Telegram Bot API

## 📦 Установка

Клонировать проект:

```bash
git clone <repository_url>
cd expense_bot
```

Создать виртуальное окружение:

```bash
python3 -m venv venv
```

Активировать:

Linux:

```bash
source venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## 🔐 Настройка

Создать файл `.env`:

```env
BOT_TOKEN=your_telegram_bot_token
```

## ▶️ Запуск

```bash
python main.py
```

## 🌐 Деплой

Проект рассчитан на запуск на VPS:

- Ubuntu 24.04 LTS
- Python virtual environment
- systemd автозапуск

## 📈 Возможное развитие

- Категории расходов
- Аналитика расходов
- Графики
- Экспорт данных
- AI-анализ финансов
- Админ-панель

## 👨‍💻 Автор

Python Backend Developer
