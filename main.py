from aiogram.utils import executor
import bot_config
from all_handlers import admin_handler, user_handler, basic_handlers


admin_handler.register_admin_handlers(bot_config.bot_dispatcher)
user_handler.register_user_handlers(bot_config.bot_dispatcher)
basic_handlers.register_basic_handlers(bot_config.bot_dispatcher)


async def on_startup(_):
    print('Enter to TG network successfully')


executor.start_polling(bot_config.bot_dispatcher, skip_updates=True, on_startup=on_startup)
