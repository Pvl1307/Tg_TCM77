import os

from dotenv import load_dotenv


# Загружаем переменные из .env
load_dotenv()


# Токен Telegram-бота
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Реферальная ссылка магазина
REFERRAL_URL = os.getenv("REFERRAL_URL")


# Проверяем наличие обязательных данных

if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN не найден в .env"
    )


if not REFERRAL_URL:
    raise ValueError(
        "REFERRAL_URL не найден в .env"
    )