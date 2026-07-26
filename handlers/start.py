from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


from keyboards.menu import main_menu


# Создаем роутер этого файла
router = Router()



@router.message(Command("start"))
async def start_command(
    message: Message
):
    """
    Первый экран после запуска бота.
    """

    await message.answer(
        text=(
            "Здравствуйте! 👋\n\n"
            "Поможем подобрать автомобиль "
            "и ответим на основные вопросы "
            "перед покупкой.\n\n"
            "Выберите, что вас интересует 👇"
        ),

        # Показываем главное меню
        reply_markup=main_menu()
    )