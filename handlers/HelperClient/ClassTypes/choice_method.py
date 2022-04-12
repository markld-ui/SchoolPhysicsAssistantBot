from aiogram import types

from loader import dp

methods_button = ['Образование (comming soon)', 'Справочник']


@dp.message_handler(lambda message: message.text == 'Да, конечно')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER---'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*methods_button)
    await message.reply('Выберите нужную для Вас опцию:', reply = False, reply_markup=keyboard)