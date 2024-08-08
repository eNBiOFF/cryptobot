from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.filters.command import CommandObject
from keyboards.inline import  get_menu_keyboard, get_start_menu
from utils.db import session, is_referral_user, get_user_by_referral_code, get_user_by_id, create_user, is_user_subscribed
from models.user import User
from config import bot
from models.referrals import Referral
from handlers.utils import is_user_subscribed

async def start_command(message: types.Message, command: CommandObject):
    user_id = message.from_user.id
    if command.args:
        referral_code = command.args 
        isReferral = await is_referral_user(bot, user_id)
        if not isReferral:
            await message.answer("Ранее вы уже были подписаны на канал, к сожалению в настоящий момент вы не можете принимать участие в реферальной программе, для начала вернитесь на канал https://t.me/testBotCharly ", reply_markup=get_start_menu())
            return
        referring_user = session.query(User).filter_by(referral_code=referral_code).first()
        if referring_user:
            if referring_user.telegram_id == user_id :
                await message.answer("Привет! К сожалению вы не можете быть рефераллом для самого себя ", reply_markup=get_menu_keyboard())
                return
            exiting_referral = session.query(Referral).filter_by(referrer_id=user_id, referred_id=referring_user.telegram_id).first()

            if exiting_referral:
                await message.answer("Привет! К сожалению вы не можете быть рефераллом для человека, которого сами пригласили ", reply_markup=get_menu_keyboard())
                return
            # Добавляем запись в таблицу referrals
            referral = Referral(referrer_id=referring_user.telegram_id, referred_id=user_id)
            session.add(referral)
            session.commit()

    user = get_user_by_id(user_id)

    isUserSubscribed = await is_user_subscribed(bot, user_id)
    markup = get_menu_keyboard() if isUserSubscribed else get_start_menu()
    if not user and isUserSubscribed:
        create_user(user_id, message.from_user.username)
    
    text = "Привет! скорее создавай реферальную ссылку, зови друзей и зарабатывай!" if isUserSubscribed else "Привет! для начала тебе нужно подписаться на канал https://t.me/testBotCharly "
    await message.answer(text, reply_markup=markup)

def register_start_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command(commands=['start']))