# main.py

"""
Главный файл запуска бота.

Здесь:
1. Загружается конфигурация.
2. Создается Bot.
3. Подключаются все обработчики.
4. Запускается polling.
"""


import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher


from config import BOT_TOKEN


from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.faq import router as faq_router



# =====================================================
# Логи только для запуска/ошибок
# =====================================================

logging.basicConfig(
    level=logging.INFO
)


logger = logging.getLogger(__name__)



# =====================================================
# Запуск бота
# =====================================================

async def main():

    # Проверяем наличие токена
    if not BOT_TOKEN:
        logger.error(
            "BOT_TOKEN не найден в .env"
        )
        sys.exit(1)


    # Создаем объект бота
    bot = Bot(
        token=BOT_TOKEN
    )


    # Создаем диспетчер
    dp = Dispatcher()



    # =================================================
    # Подключаем обработчики
    # Порядок важен
    # =================================================

    dp.include_router(
        start_router
    )

    dp.include_router(
        menu_router
    )

    dp.include_router(
        faq_router
    )



    logger.info(
        "Бот запущен"
    )


    # Запускаем получение сообщений
    await dp.start_polling(
        bot
    )



# =====================================================
# Точка входа
# =====================================================

if __name__ == "__main__":
    asyncio.run(main())