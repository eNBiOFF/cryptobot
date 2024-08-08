
import asyncio
import logging
from config import dp, bot
from handlers import register_handlers
from utils.db import init_db

async def main():
    async def custom_middleware(handler, event, data):
        logging.info(f'Update: {event}')
        return await handler(event, data)

    dp.update.outer_middleware(custom_middleware)
    
    init_db()
    logging.info("Database initialized")

    register_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())