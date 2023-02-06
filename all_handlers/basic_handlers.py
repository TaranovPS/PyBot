from all_handlers.father import *


#@bot_dispatcher.message_handler(commands='start')
async def start_bot_button(message: types.Message):
    if message.from_user.id in bot_config.users:
        await bot.send_message(message.from_user.id, f'Привет, {bot_config.users[message.from_user.id]}', reply_markup=basic_keyboards.user_kb)
    elif message.from_user.id in bot_config.admin_users:
        await bot.send_message(message.from_user.id, 'Привет Админ!', reply_markup=basic_keyboards.admin_kb)
    else:
        await bot.send_message(message.from_user.id, 'Кто ты, игрок?', reply_markup=basic_keyboards.start_kb)


#@bot_dispatcher.message_handler()
async def dont_know(message: types.Message):
    await message.reply('I do not know')


def register_basic_handlers(dp):
    dp.register_message_handler(start_bot_button, commands='start')
    dp.register_message_handler(dont_know)



