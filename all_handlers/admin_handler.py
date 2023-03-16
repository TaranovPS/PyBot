from all_handlers.father import *


class AdminState(StatesGroup):
    admin_check = State()
    admin_name = State()


async def check_admin(message:types.Message):
    if message.from_user.id not in bot_config.admin_users:
        await AdminState.admin_check.set()
        await bot.send_message(message.from_user.id, 'Докажи! Введи секретный шифр!')
    else:
        await bot.send_message(message.from_user.id, 'Капитан, у вас деменция! Вы и так капитан, выше некуда!', reply_markup=basic_keyboards.admin_kb)


async def new_admin_check(message:types.Message, state=FSMContext):
    if message.text == bot_config.admin_password:
        await bot.send_message(message.from_user.id, 'Хорошо. Как вас будет звать команда?')
        await AdminState.next()
    else:
        await bot.send_message(message.from_user.id, 'Кажется, капитан, на кухне скопилось много посуды, соизволите помыть?',
                               reply_markup=basic_keyboards.start_kb)
        await state.finish()


async def create_new_admin(message:types.Message, state=FSMContext):
    bot_config.admin_users[message.from_user.id] = message.text + '-' + random.choice(bot_config.unique_names)
    await bot.send_message(message.from_user.id, f'Будем называть тебя {bot_config.admin_users[message.from_user.id]}',
                           reply_markup=basic_keyboards.admin_kb)
    await state.finish()


async def change_admin_role(message: types.Message):
    try:
        del bot_config.admin_users[message.from_user.id]
        await bot.send_message(message.from_user.id,
                               'Хочешь мыть посуду как эти береговые крысы? Хорошо!',
                               reply_markup=basic_keyboards.start_kb)
    except:
        await bot.send_message(message.from_user.id, 'Ты и так палубная крыса!', reply_markup=basic_keyboards.start_kb)


async def show_result(message: types.Message):
    bot.send_message(message.from_user.id, 'Твоя команда сделала сегодня что то', reply_markup=basic_keyboards.admin_kb)


def register_admin_handlers(dp):
    dp.register_message_handler(check_admin, lambda message: message.text == 'Я Капитан!', state=None)
    dp.register_message_handler(new_admin_check, state=AdminState.admin_check)
    dp.register_message_handler(create_new_admin, state=AdminState.admin_name)
    dp.register_message_handler(change_admin_role, lambda message: message.text == 'Меня понизили!')
    dp.register_message_handler(show_result, lambda message: message.text == 'Показать результат команды!')

