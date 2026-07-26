from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import REFERRAL_URL


# =====================================================
# Главное меню после /start
# =====================================================

def main_menu() -> ReplyKeyboardMarkup:
    """
    Главное меню клиента.
    Используем обычную клавиатуру только на старте.
    """

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🚗 Я определился с выбором"
                )
            ],
            [
                KeyboardButton(
                    text="🤔 Мне нужна помощь с выбором"
                )
            ],
            [
                KeyboardButton(
                    text="💬 Остались вопросы?"
                )
            ],
        ],
        resize_keyboard=True,
    )


# =====================================================
# Кнопка перехода по реферальной ссылке
# =====================================================

def referral_keyboard(text: str) -> InlineKeyboardMarkup:
    """
    Inline-кнопка с нашей реферальной ссылкой.

    text - название кнопки,
    REFERRAL_URL - ссылка магазина из .env
    """

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text,
                    url=REFERRAL_URL
                )
            ]
        ]
    )


# =====================================================
# Меню FAQ
# =====================================================

def faq_menu() -> InlineKeyboardMarkup:
    """
    Список частых вопросов.
    """

    questions = [
        (
            "🚚 Сколько ждать автомобиль?",
            "waiting"
        ),
        (
            "💳 Как проходит оплата?",
            "payment"
        ),
        (
            "🏦 Можно ли купить в кредит?",
            "credit"
        ),
        (
            "💰 Откуда берётся итоговая цена?",
            "price"
        ),
        (
            "🛃 Что с таможней и гарантиями?",
            "customs"
        ),
        (
            "🅿️ Где хранится автомобиль?",
            "storage"
        ),
        (
            "🌍 С какими странами работаете?",
            "countries"
        ),
        (
            "📄 Что входит в бронь?",
            "booking"
        ),
        (
            "🤝 Какие гарантии?",
            "guarantees"
        ),
        (
            "📞 Не нашли ответ?",
            "manager"
        ),
    ]


    buttons = []

    for text, callback in questions:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=text,
                    callback_data=f"faq:{callback}"
                )
            ]
        )


    return InlineKeyboardMarkup(
        inline_keyboard=buttons
    )


# =====================================================
# Возврат обратно к вопросам
# =====================================================

def back_to_faq_keyboard() -> InlineKeyboardMarkup:
    """
    Кнопка после ответа FAQ.
    """

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅️ Вернуться к вопросам",
                    callback_data="back_to_faq"
                )
            ]
        ]
    )


# =====================================================
# Кнопка менеджера
# =====================================================

def manager_keyboard() -> InlineKeyboardMarkup:
    """
    Ссылка на менеджера через реферальную ссылку.
    """

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👉 Обратиться к менеджеру",
                    url=REFERRAL_URL
                )
            ]
        ]
    )