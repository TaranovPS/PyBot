from all_handlers.father import *


class UserState(StatesGroup):
    user_state = State()


#@bot_dispatcher.message_handler(commands='user', state=None)
async def remember_my_uniq_user_name(message: types.Message):
    if message.from_user.id in bot_config.users:
        await bot.send_message(message.from_user.id, 'Ты уже старенький, иди в свое меню!', reply_markup=basic_keyboards.user_kb)
    else:
        await UserState.user_state.set()
        await bot.send_message(message.from_user.id, 'Ты тут новенький! Как тебя зовут?')


#@bot_dispatcher.message_handler(state=UserState.user_state)
async def create_user_uniq_name(message: types.Message, state: FSMContext):
    bot_config.users[message.from_user.id] = message.text + '-' + random.choice(bot_config.unique_names)
    await state.finish()
    await bot.send_message(message.from_user.id, f'Будем называть тебя {bot_config.users[message.from_user.id]}', reply_markup=basic_keyboards.user_kb)


def register_user_handlers(dp):
    dp.register_message_handler(remember_my_uniq_user_name, commands='user', state=None)
    dp.register_message_handler(create_user_uniq_name, state=UserState.user_state)