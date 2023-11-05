from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@dp.message(lambda message: message.text == 'Нет')
async def disagree(message: types.Message):
    '''DISAGREE FUNCTION IF USER WANTED GET MORE INFO ABOUT BOT'''
    array_disagree = [
        [KeyboardButton(text='Кем разработан этот проект?')],
        [KeyboardButton(text='Спасибо, можем приступать.')],
        ]
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_disagree], resize_keyboard = True)
    await message.reply('Что бы вы хотели узнать ещё?',
        reply = False,
        reply_markup = keyboard)