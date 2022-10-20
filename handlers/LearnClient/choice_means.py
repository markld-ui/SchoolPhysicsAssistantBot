from aiogram import types

from loader import dp

types_button = ['Видеоуроки', 'Презентации', 'Задачи','Выйти к выбору операции']


@dp.message_handler(lambda message: message.text == 'Образование')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER IN EDUCATION---'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*types_button)
    await message.reply('Чем хотите воспользоваться?', reply = False, reply_markup=keyboard)