# handlers/menu.py

"""
Обработчики главного меню.

Здесь находятся:
1. 🚗 Я определился с выбором
2. 🤔 Мне нужна помощь с выбором
3. 💬 Остались вопросы
"""


from aiogram import Router, F
from aiogram.types import Message


from keyboards.menu import (
    faq_menu,
    referral_keyboard,
)


from services.referral import get_referral_link



router = Router()



# =====================================================
# 🚗 Клиент определился с автомобилем
# =====================================================

@router.message(
    F.text == "🚗 Я определился с выбором"
)
async def selected_car(
    message: Message
):
    """
    Клиент уже знает, что хочет.

    Отправляем его сразу на магазин
    через нашу реферальную ссылку.
    """


    await message.answer(
        text=(
            "<b>Отлично! 🚗</b>\n\n"
            "Перейдите по ссылке ниже, чтобы "
            "посмотреть доступные автомобили "
            "и оформить заявку:"
        ),
        parse_mode="HTML",
        reply_markup=referral_keyboard(
            "👉 Перейти к выбору автомобиля"
        )
    )



# =====================================================
# 🤔 Нужна помощь с выбором
# =====================================================

@router.message(
    F.text == "🤔 Мне нужна помощь с выбором"
)
async def need_help(
    message: Message
):
    """
    Клиент хочет консультацию.
    """

    await message.answer(
        text=(
            "<b>Поможем подобрать автомобиль 🚗</b>\n\n"
            "Оставьте заявку, и менеджер поможет "
            "с выбором подходящего варианта:"
        ),
        parse_mode="HTML",
        reply_markup=referral_keyboard(
            "👉 Получить помощь менеджера"
        )
    )



# =====================================================
# 💬 FAQ
# =====================================================

@router.message(
    F.text == "💬 Остались вопросы?"
)
async def questions(
    message: Message
):
    """
    Открываем раздел FAQ.

    ReplyKeyboard больше не показываем.
    Только inline-кнопки.
    """


    await message.answer(
        text=(
            "<b>💬 Остались вопросы?</b>\n\n"
            "Собрали вопросы, которые нам "
            "задают чаще всего.\n\n"
            "Выберите интересующий 👇"
        ),
        parse_mode="HTML",
        reply_markup=faq_menu()
    )