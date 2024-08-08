
from aiogram import types, Dispatcher
from aiogram.filters import Text
from keyboards.inline import get_menu_keyboard
from utils.db import session, get_user_by_id, get_refferal_entity
from handlers.utils import is_user_subscribed
from models.user import User
from config import bot

async def subscribed_command(callback_qury: types.callback_query ):
    is_user_sub = is_user_subscribed(bot, user_id= callback_qury.from_user.id)
    user = get_user_by_id(callback_qury.from_user.id)
    
    
    if not user and is_user_sub:
        user = User(
            telegram_id=callback_qury.from_user.id,
            username=callback_qury.from_user.username,
        )
        referral_entity = get_refferal_entity(callback_qury.from_user.id)
        chat_member = await bot.get_chat_member(chat_id='-1001875239946', user_id=user.telegram_id)
        is_chat_member_status_left = chat_member.status == 'left'
        if referral_entity and not is_chat_member_status_left :
            referral_user = get_user_by_id(referral_entity.referrer_id)
            referral_user.balance = referral_user.balance + 10
        session.add(user)
        session.commit()
        await callback_qury.message.edit_text(
            f"Привет, {callback_qury.from_user.full_name}! теперь ты можешь использовать все функции бота!",
            reply_markup=get_menu_keyboard()
        ) 
    else: 
        await callback_qury.message.edit_text(
            f"Привет, {callback_qury.from_user.full_name}! похоже ты еще не подписан на канал",
            reply_markup=get_menu_keyboard()
        )

def register_subscribed_handlers(dp: Dispatcher):
    dp.callback_query.register(subscribed_command, Text(text=['subscribed']))