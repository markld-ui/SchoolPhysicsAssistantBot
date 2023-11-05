from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

methods_button = [
    [KeyboardButton(text='Образование')],
    [KeyboardButton(text='Справочник')],
]


@dp.message(lambda message: message.text == 'Да, конечно')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER---'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*methods_button], resize_keyboard = True)
    await message.reply('Выберите нужную для Вас опцию:', reply = False, reply_markup=keyboard)