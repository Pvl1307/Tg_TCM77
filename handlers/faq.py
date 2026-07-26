from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.menu import (
    faq_menu,
    back_to_faq_keyboard,
    manager_keyboard,
)

from services.faq import get_faq_answer


router = Router()



# =====================================================
# Пользователь не нашел ответ
# =====================================================

@router.callback_query(
    F.data == "faq:manager"
)
async def faq_manager(
    callback: CallbackQuery
):

    await callback.answer()

    await callback.message.answer(
        text=(
            "<b>📞 Не нашли ответ на свой вопрос?</b>\n\n"
            "Свяжитесь с менеджером — он поможет "
            "подобрать автомобиль и ответит на все вопросы."
        ),
        parse_mode="HTML",
        reply_markup=manager_keyboard()
    )



# =====================================================
# Ответы FAQ
# =====================================================

@router.callback_query(
    F.data.startswith("faq:")
)
async def show_faq_answer(
    callback: CallbackQuery
):

    await callback.answer()


    key = callback.data.split(":")[1]


    answer = get_faq_answer(key)


    if not answer:
        await callback.message.answer(
            "Ответ пока не добавлен."
        )
        return


    await callback.message.answer(
        text=answer,
        parse_mode="HTML",
        reply_markup=back_to_faq_keyboard()
    )



# =====================================================
# Вернуться к списку вопросов
# =====================================================

@router.callback_query(
    F.data == "back_to_faq"
)
async def back_to_questions(
    callback: CallbackQuery
):

    await callback.answer()


    await callback.message.answer(
        text=(
            "<b>💬 Остались вопросы?</b>\n\n"
            "Собрали вопросы, которые нам "
            "задают чаще всего.\n\n"
            "Выберите интересующий 👇"
        ),
        parse_mode="HTML",
        reply_markup=faq_menu()
    )