from aiogram.utils import executor
import bot_config
from all_handlers import admin_handler, user_handler, basic_handlers
import sql_config
import asyncio
import aioschedule


admin_handler.register_admin_handlers(bot_config.bot_dispatcher)
user_handler.register_user_handlers(bot_config.bot_dispatcher)
basic_handlers.register_basic_handlers(bot_config.bot_dispatcher)


async def noon_print():
    for i in bot_config.admin_users:
        await bot_config.bot.send_message(i, f'Твоя команда сделала сегодня None')


async def scheduler():
    aioschedule.every().day.at("21:27").do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())
    print('Enter to TG network successfully')


if __name__ == '__main__':
    executor.start_polling(bot_config.bot_dispatcher, skip_updates=True, on_startup=on_startup)


