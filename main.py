from aiogram.utils import executor
import bot_config
import handlers


async def on_startup(_):
    print('Enter to TG network successfully')


executor.start_polling(bot_config.bot_dispatcher, skip_updates=True, on_startup=on_startup)
