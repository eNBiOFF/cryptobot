from utils.db import generate_referral_link
from aiogram import Dispatcher, types
from aiogram.filters import Text
from keyboards.inline import get_menu_keyboard
from config import bot

async def referral_link(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    referral_link = generate_referral_link(user_id)
    await callback_query.message.edit_text(f"Ваша реферальная ссылка: {referral_link}", reply_markup=get_menu_keyboard())

def register_referral_link(dp: Dispatcher):
    dp.callback_query.register(referral_link, Text(text=['referral_link']))
