from pydantic import BaseSettings
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import logging

class Config(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

config = Config()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)