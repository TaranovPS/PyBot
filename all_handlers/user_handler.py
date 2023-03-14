from all_handlers.father import *


class UserState(StatesGroup):
    user_state = State()


async def remember_my_uniq_user_name(message: types.Message):
    if message.from_user.id in bot_config.users:
        await bot.send_message(message.from_user.id, 'Куда ты к штурвалу лезешь салага? Бери тряпку и за работу!', reply_markup=basic_keyboards.user_kb)
    else:
        await UserState.user_state.set()
        await bot.send_message(message.from_user.id, 'Ты тут новенький! Как тебя зовут?')


async def create_user_uniq_name(message: types.Message, state: FSMContext):
    bot_config.users[message.from_user.id] = message.text + '-' + random.choice(bot_config.unique_names)
    await state.finish()
    await bot.send_message(message.from_user.id, f'Будем называть тебя {bot_config.users[message.from_user.id]}', reply_markup=basic_keyboards.user_kb)


async def change_user_name(message: types.Message):
    try:
        bot_config.users[message.from_user.id] = bot_config.users[message.from_user.id].split('-')[0] + '-' + random.choice(bot_config.unique_names)
        await bot.send_message(message.from_user.id, f'Ты хочешь новое имя? Будет! Теперь ты {bot_config.users[message.from_user.id]}', reply_markup=basic_keyboards.user_kb)
    except:
        await bot.send_message(message.from_user.id, 'Кажется тебя нет в списке салаг(', reply_markup=basic_keyboards.start_kb)


async def change_user_role(message: types.Message):
    try:
        del bot_config.users[message.from_user.id]
        await bot.send_message(message.from_user.id, 'Смотрите ка, повышение!', reply_markup=basic_keyboards.start_kb)
    except:
        await bot.send_message(message.from_user.id, 'Кажется ошибка', reply_markup=basic_keyboards.start_kb)


def register_user_handlers(dp):
    dp.register_message_handler(remember_my_uniq_user_name, lambda message: message.text == 'Я рядовой Шкет!', state=None)
    dp.register_message_handler(create_user_uniq_name, state=UserState.user_state)
    dp.register_message_handler(change_user_name, lambda message: message.text == 'Сменить кличку')
    dp.register_message_handler(change_user_role, lambda message: message.text == 'Я теперь Капитан!')