from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start_admin_keyboard = KeyboardButton('/admin')
start_user_keyboard = KeyboardButton('/user')

main_user_keyboard_1 = KeyboardButton('/ChangeName')
main_user_keyboard_2 = KeyboardButton('/Result')
main_user_keyboard_3 = KeyboardButton('/ChangeResult')
main_user_keyboard_4 = KeyboardButton('/Show')


main_admin_keyboard_1 = KeyboardButton('/ShowAll')
main_admin_keyboard_2 = KeyboardButton('/SelectOne')



start_kb = ReplyKeyboardMarkup()
start_kb.add(start_admin_keyboard).add(start_user_keyboard)

user_kb = ReplyKeyboardMarkup()
user_kb.add(main_user_keyboard_4).add(main_user_keyboard_3).add(main_user_keyboard_2).add(main_user_keyboard_1)


admin_kb = ReplyKeyboardMarkup()
admin_kb.add(main_admin_keyboard_1).add(main_admin_keyboard_2)

