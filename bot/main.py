import asyncio

from bot.bot import bot, dp
from handlers.handlers import router
from handlers.callbacks import router_for_callbacks
from handlers.admin import router_admin

if __name__ == '__main__':
    dp.include_router(router)
    dp.include_router(router_for_callbacks)
    dp.include_router(router_admin)


    async def main():
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


    asyncio.run(main())