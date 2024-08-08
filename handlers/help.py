from aiogram import types, Dispatcher
from aiogram.filters import Command, Text

async def help_command(message: types.Message):
    await message.answer("Этот бот использует aiogram и SQLAlchemy. Доступные команды: /start, /help")

async def help_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Этот бот использует aiogram и SQLAlchemy. Доступные команды: /start, /help")
    await callback_query.answer()

def register_help_handlers(dp: Dispatcher):
    dp.message.register(help_command, Command(commands=['help']))
    dp.callback_query.register(help_callback, Text(text="help"))