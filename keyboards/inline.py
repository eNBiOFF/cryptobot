from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_help_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Помощь", callback_data="help")],
            [InlineKeyboardButton(text="Реферальная ссылка", callback_data="referral_link")]
        ]
    )

def get_menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Баланс", callback_data="balance")],
            [InlineKeyboardButton(text="Реферальная ссылка", callback_data="referral_link")]
        ]
    )

def get_start_menu(): 
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Подписался", callback_data="subscribed")]
        ]
    )