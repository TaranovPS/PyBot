import sql_config
from all_handlers.father import *


res_day = {}


class UserState(StatesGroup):
    user_state = State()


class ResultState(StatesGroup):
    cash = State()
    heads = State()
    sales = State()


async def remember_my_uniq_user_name(message: types.Message):
    if not await sql_config.check_if_user(message.from_user.id):
        await message.reply('Тебя нет в списке!', reply_markup=basic_keyboards.start_kb)
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


async def save_result(message: types.Message):
    if not sql_config.cursor.execute(f'SELECT * FROM result WHERE id = {message.from_user.id} AND date = "{str(datetime.date.today())}"')\
            and sql_config.cursor.execute(f'SELECT * FROM users WHERE id = {message.from_user.id}'):
        await ResultState.cash.set()
        await bot.send_message(message.from_user.id, 'Сколько заработал денег сегодня?')
    else:
        await bot.send_message(message.from_user.id, 'Ты уже записывал результат дня или тебя нет в списке!', reply_markup=types.ReplyKeyboardRemove())


async def save_cash_result(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await bot.send_message(message.from_user.id, 'Введи число! Что непонятного? Начни сначала', reply_markup=basic_keyboards.user_kb)
    else:
        res_day[message.from_user.id] = [message.text]
        await bot.send_message(message.from_user.id, 'А теперь - сколько принес голов?', reply_markup=types.ReplyKeyboardRemove())
        await ResultState.next()


async def save_heads_result(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await bot.send_message(message.from_user.id, 'Введи число! Что непонятного? Начни сначала', reply_markup=basic_keyboards.user_kb)
    else:
        res_day[message.from_user.id].append(message.text)
        await bot.send_message(message.from_user.id, 'А теперь - сколько принес продаж?')
        await ResultState.next()


async def save_sales_result(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await bot.send_message(message.from_user.id, 'Введи число! Что непонятного? Начни сначала', reply_markup=basic_keyboards.user_kb)
    else:
        res_day[message.from_user.id].append(message.text)
        await sql_config.sql_load_data_to_result(message.from_user.id, bot_config.users[message.from_user.id],
                                       res_day[message.from_user.id][0],
                                       res_day[message.from_user.id][1], res_day[message.from_user.id][2])
        await bot.send_message(message.from_user.id, 'Отлично', reply_markup=basic_keyboards.user_kb)
        await state.finish()


def register_user_handlers(dp):
    dp.register_message_handler(remember_my_uniq_user_name, lambda message: message.text == 'Я рядовой Шкет!', state=None)
    dp.register_message_handler(create_user_uniq_name, state=UserState.user_state)
    dp.register_message_handler(save_result, lambda message: message.text == 'Записать результат дня')
    dp.register_message_handler(save_cash_result, state=ResultState.cash)
    dp.register_message_handler(save_heads_result, state=ResultState.heads)
    dp.register_message_handler(save_sales_result, state=ResultState.sales)
    dp.register_message_handler(change_user_name, lambda message: message.text == 'Сменить кличку')
    dp.register_message_handler(change_user_role, lambda message: message.text == 'Я теперь Капитан!')