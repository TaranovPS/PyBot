from aiogram import Dispatcher as dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

class FSM_admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


@dp.message_handler(commands='Admin', state=None)
async def fix_data(message: types.message):
    await FSM_admin.photo.set()
    await message.reply('Загрузи фото')


dp.message_handler(content_types=['photo'], state=FSM_admin.photo)
async def load_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSM_admin.next()
    await message.reply('А теперь название')


dp.message_handler()
