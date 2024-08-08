from aiogram import types, Dispatcher
from aiogram.filters import Text
from utils.db import get_user_by_id
from keyboards.inline import get_menu_keyboard
from models.user import User
from config import bot

async def balance_callback(callback_query: types.CallbackQuery):
    user = get_user_by_id(callback_query.from_user.id)
    if user:
        await callback_query.message.edit_text(f"Ваш баланс: {user.balance:.2f}", reply_markup=get_menu_keyboard())
    else:
        await callback_query.message.edit_text("Вы не подписаны на канал. Используйте команду /start для регистрации.")
    await callback_query.answer()

def register_balance_handlers(dp: Dispatcher):
    dp.callback_query.register(balance_callback, Text(text="balance"))