from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN = '6135333642:AAElrgX6p2wUc4Nbct2EAhC0bx8_cDSgpMk'
storage = MemoryStorage()


bot = Bot(token=TOKEN)
bot_dispatcher = Dispatcher(bot, storage=storage)


admin_password = '1234'
admin_users = {}


users = {}
unique_names = ['Корявая Нога', 'Вырви Глаз', 'Сломаный череп', 'Четырехпалый', 'Кровавое копыто',
                'Земляной крот', 'Подмышка Ежа', 'Костоправ', 'Величайший', 'Дурная кровь', 'Мошонка Кабана',
                'Очаковское светлое', 'Кошачья мята']

