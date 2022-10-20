from aiogram import types

from loader import dp

class_button = ['7v', '8v', '9v','10v', '11v', 'Выйти к выбору способов']


@dp.message_handler(lambda message: message.text == 'Видеоуроки')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER IN EDUCATION---'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply = False, reply_markup=keyboard)