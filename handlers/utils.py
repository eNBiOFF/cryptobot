from aiogram.exceptions import TelegramNotFound  
from utils.db import get_user_by_id

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