from all_handlers.father import *


class AdminState(StatesGroup):
    admin_check = State()
    admin_name = State()


#@bot_dispatcher.message_handler(commands='admin', state=None)
async def check_admin(message:types.Message):
    if message.from_user.id not in bot_config.admin_users:
        await AdminState.admin_check.set()
        await bot.send_message(message.from_user.id, 'Докажи! Введи секретный шифр!')
    else:
        await bot.send_message(message.from_user.id, 'Ты и так Админ!', reply_markup=basic_keyboards.admin_kb)


#@bot_dispatcher.message_handler(state=AdminState.admin_check)
async def new_admin_check(message:types.Message, state=FSMContext):
    if message.text == bot_config.admin_password:
        await bot.send_message(message.from_user.id, 'Хорошо, допустим. А как нам называть тебя?')
        await AdminState.next()
    else:
        await bot.send_message(message.from_user.id, 'Иди обманывай в другое место, кыш на стартовое меню!', reply_markup=basic_keyboards.start_kb)
        await state.finish()


#@bot_dispatcher.message_handler(state=AdminState.admin_name)
async def create_new_admin(message:types.Message, state=FSMContext):
    bot_config.admin_users[message.from_user.id] = message.text + '-' + random.choice(bot_config.unique_names)
    await bot.send_message(message.from_user.id, f'Будем называть тебя {bot_config.admin_users[message.from_user.id]}',
                           reply_markup=basic_keyboards.admin_kb)
    await state.finish()


def register_admin_handlers(dp):
    dp.register_message_handler(check_admin, commands='admin', state=None)
    dp.register_message_handler(new_admin_check, state=AdminState.admin_check)
    dp.register_message_handler(create_new_admin, state=AdminState.admin_name)
