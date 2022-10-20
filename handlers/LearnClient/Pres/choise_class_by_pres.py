from aiogram import types

from loader import dp

class_button = ['7p', '8p', '9p','10p', '11p', 'Выйти к выбору способов']


@dp.message_handler(lambda message: message.text == 'Презентации')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER IN EDUCATION---'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply = False, reply_markup=keyboard)