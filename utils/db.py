
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from aiogram.exceptions import TelegramNotFound
from config import config
from models import Base
from models.user import User
from models.referrals import Referral
import uuid

DATABASE_URL = config.DATABASE_URL

engine = create_engine(f'sqlite:///referrals.db', echo=True)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def init_db():
    Base.metadata.create_all(engine)

def create_user(id, username=None, chat_id=None, referral_code=None):
    user = User(telegram_id=id, username=username, chat_id=chat_id, referral_code=referral_code)
    session.add(user)
    session.commit()
    return user

def get_user_by_id(user_id):
    return session.query(User).filter_by(telegram_id=user_id).first()

def get_user_by_referral_code(referral_code):
    return session.query(User).filter_by(referral_code=referral_code).first()

def get_refferal_entity(reffering_code): 
    return session.query(Referral).filter_by(referred_id=reffering_code).first()

def generate_referral_link(user_id):
    user = get_user_by_id(user_id)
    if user:
        referral_code = user.referral_code
        if not referral_code:
            referral_code = str(uuid.uuid4())[:8]  # Генерируем уникальный код для ссылки
            user.referral_code = referral_code
            session.commit()

    # Реализация генерации реферальной ссылки
    return f"https://t.me/chalry_m_bot?start={referral_code}"  # Приме

async def is_user_subscribed(bot, user_id):
    try:
        # Получаем информацию о пользователе в канале
        chat_member = await bot.get_chat_member(chat_id='-1001875239946', user_id=user_id)
        # Проверяем статус пользователя в канале
        if chat_member.status == 'member' or chat_member.status == 'creator' or chat_member.status == 'administrator':
            return True
        else:
            return False
    except TelegramNotFound as e:
        print(f"Ошибка при получении информации о пользователе: {e}")
        return False
    
async def is_referral_user(bot, user_id): 
    try: 
        chat_member = await bot.get_chat_member(chat_id='-1001875239946', user_id=user_id)
        user = get_user_by_id(user_id)
        if chat_member.status == 'left' and user: 
            return False
        else:
            return True
    except TelegramNotFound as e:
        print(f"Ошибка при получении информации о пользователе: {e}")
        return False