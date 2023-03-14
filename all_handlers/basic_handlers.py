from all_handlers.father import *


async def start_bot_button(message: types.Message):
    if message.from_user.id in bot_config.users:
        await bot.send_message(message.from_user.id, f'Опять ты, крыса помойная, бери тряпку и за работу! '
                                                     f'{bot_config.users[message.from_user.id]}',
                               reply_markup=basic_keyboards.user_kb)
    elif message.from_user.id in bot_config.admin_users:
        await bot.send_message(message.from_user.id, 'Привет Капитан!', reply_markup=basic_keyboards.admin_kb)
    else:
        await bot.send_message(message.from_user.id, 'Аррр! Добро пожаловать на борт нашего корабля! '
                                                     'Ты новый капитан или новый салага?',
                               reply_markup=basic_keyboards.start_kb)


async def dont_know(message: types.Message):
    await message.reply('О чем это ты там бормочешь?')


def register_basic_handlers(dp):
    dp.register_message_handler(start_bot_button, commands='start')
    dp.register_message_handler(dont_know)
