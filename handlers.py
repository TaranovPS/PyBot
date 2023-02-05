import bot_config
from bot_config import bot_dispatcher, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
import basic_keyboards
import sql_config
import random


class UserState(StatesGroup):
    user_state = State()


class AdminState(StatesGroup):
    admin_check = State()
    admin_name = State()



@bot_dispatcher.message_handler(commands='start')
async def start_bot_button(message: types.Message):
    if message.from_user.id in bot_config.users:
        await bot.send_message(message.from_user.id, f'Привет, {bot_config.users[message.from_user.id]}', reply_markup=basic_keyboards.user_kb)
    elif message.from_user.id in bot_config.admin_users:
        await bot.send_message(message.from_user.id, 'Привет Админ!', reply_markup=basic_keyboards.admin_kb)
    else:
        await bot.send_message(message.from_user.id, 'Кто ты, игрок?', reply_markup=basic_keyboards.start_kb)


@bot_dispatcher.message_handler(commands='user', state=None)
async def remember_my_uniq_user_name(message: types.Message):
    if message.from_user.id in bot_config.users:
        await bot.send_message(message.from_user.id, 'Ты уже старенький, иди в свое меню!', reply_markup=basic_keyboards.user_kb)
    else:
        await UserState.user_state.set()
        await bot.send_message(message.from_user.id, 'Ты тут новенький! Как тебя зовут?')


@bot_dispatcher.message_handler(commands='admin', state=None)
async def check_admin(message:types.Message):
    if message.from_user.id not in bot_config.admin_users:
        await AdminState.admin_check.set()
        await bot.send_message(message.from_user.id, 'Докажи! Введи секретный шифр!')
    else:
        await bot.send_message(message.from_user.id, 'Ты и так Админ!', reply_markup=basic_keyboards.admin_kb)


@bot_dispatcher.message_handler(state=AdminState.admin_check)
async def new_admin_check(message:types.Message, state=FSMContext):
    if message.text == bot_config.admin_password:
        await bot.send_message(message.from_user.id, 'Хорошо, допустим. А как нам называть тебя?')
        await AdminState.next()
    else:
        await bot.send_message(message.from_user.id, 'Иди обманывай в другое место, кыш на стартовое меню!', reply_markup=basic_keyboards.start_kb)
        await state.finish()


@bot_dispatcher.message_handler(state=AdminState.admin_name)
async def create_new_admin(message:types.Message, state=FSMContext):
    bot_config.admin_users[message.from_user.id] = message.text + '-' + random.choice(bot_config.unique_names)
    await bot.send_message(message.from_user.id, f'Будем называть тебя {bot_config.admin_users[message.from_user.id]}',
                           reply_markup=basic_keyboards.admin_kb)
    await state.finish()


@bot_dispatcher.message_handler(state=UserState.user_state)
async def create_user_uniq_name(message: types.Message, state: FSMContext):
    bot_config.users[message.from_user.id] = message.text + '-' + random.choice(bot_config.unique_names)
    await state.finish()
    await bot.send_message(message.from_user.id, f'Будем называть тебя {bot_config.users[message.from_user.id]}', reply_markup=basic_keyboards.user_kb)


@bot_dispatcher.message_handler()
async def dont_know(message: types.Message):
    await message.reply('I do not know')




