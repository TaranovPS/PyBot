from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start_admin_keyboard = KeyboardButton('Я админ!')
start_user_keyboard = KeyboardButton('Я юзер!')


main_user_keyboard_1 = KeyboardButton('Сменить имя')
main_user_keyboard_2 = KeyboardButton('Записать результат дня')
main_user_keyboard_3 = KeyboardButton('Изменить результат дня')
main_user_keyboard_4 = KeyboardButton('Показать результат за день')
main_user_keyboard_5 = KeyboardButton('Я теперь Админ!')


main_admin_keyboard_1 = KeyboardButton('Показать результат группы')
main_admin_keyboard_2 = KeyboardButton('Я теперь юзер!')


start_kb = ReplyKeyboardMarkup()
start_kb.add(start_admin_keyboard).add(start_user_keyboard)


user_kb = ReplyKeyboardMarkup()
user_kb.add(main_user_keyboard_4).add(main_user_keyboard_3).add(main_user_keyboard_2).add(main_user_keyboard_1).add(main_user_keyboard_5)


admin_kb = ReplyKeyboardMarkup()
admin_kb.add(main_admin_keyboard_1).add(main_admin_keyboard_2)

