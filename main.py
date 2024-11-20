import asyncio
import logging

from aiogram import Bot, Dispatcher

import config as c
from app.user.user_handlers import userRouter
from app.admin.admin_handlers import adminRouter
from app.mini_games.game_handlers import gameRouter
from app.database.models import async_main


logging.basicConfig(level = logging.INFO)
bot = Bot(token = c.api_token)
dp = Dispatcher()


async def main():
    await async_main()
    await bot.delete_webhook(drop_pending_updates = True)
    dp.include_router(userRouter)
    dp.include_router(adminRouter)
    dp.include_router(gameRouter)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("INFO.aiogram.dispatcher:Stop updates/working - bot is offline")