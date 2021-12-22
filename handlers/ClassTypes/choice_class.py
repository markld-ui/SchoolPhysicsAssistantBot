from aiogram import types

from loader import dp

class_button = ['7 класс', '8 класс', '9 класс', '10 класс', '11 класс']


@dp.message_handler(lambda message: message.text == 'Да, конечно')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER---'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply = False, reply_markup=keyboard)