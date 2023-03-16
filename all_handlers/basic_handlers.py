import sql_config
from all_handlers.father import *


async def start_bot_button(message: types.Message):
    if await sql_config.check_if_user(message.from_user.id):
        await message.answer(f'Опять ты, крыса помойная, бери тряпку и за работу!',
                             reply_markup=basic_keyboards.user_kb)
    elif await sql_config.check_if_admin(message.from_user.id):
        await message.answer('Привет Капитан!', reply_markup=basic_keyboards.admin_kb)
    else:
        await message.answer('Аррр! Добро пожаловать на борт нашего корабля! '
                             'Ты новый капитан или новый салага?',
                             reply_markup=basic_keyboards.start_kb)


async def dont_know(message: types.Message):
    await message.reply('О чем это ты там бормочешь?')


def register_basic_handlers(dp):
    dp.register_message_handler(start_bot_button, commands='start')
    dp.register_message_handler(dont_know)
