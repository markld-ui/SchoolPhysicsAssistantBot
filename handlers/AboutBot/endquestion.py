from aiogram import types

from loader import dp
from handlers.HelperClient.ClassTypes.choice_method import methods_button
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup

@dp.message(lambda message: message.text == 'Спасибо, можем приступать.')
async def agree(message: types.Message):
    '''AGREE FUNCTION IF USER RECEIVED ENOUGH INFO ABOUT BOT'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*methods_button],resize_keyboard = True)
    await message.reply('Выберите свою опцию', reply = False, reply_markup=keyboard)