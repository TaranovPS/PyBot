from aiogram.utils import executor
import sql_config
import bot_config
import all_handlers
bd = bot_config.bot_dispatcher
all_handlers.admin_handler.register_admin_handlers(bd)
all_handlers.user_handler.register_user_handlers(bd)
all_handlers.basic_handlers.register_basic_handlers(bd)


async def on_startup(_):
    print('Enter to TG network successfully')


executor.start_polling(bd, skip_updates=True, on_startup=on_startup)
