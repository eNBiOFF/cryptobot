from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_default_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пример кнопки")]
        ],
        resize_keyboard=True
    )