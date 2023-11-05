from aiogram import types
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup

from loader import dp
from handlers.HelperClient.ClassTypes.choice_method import methods_button

@dp.message(lambda message: message.text == 'Да')
async def agree(message: types.Message):
    '''AGREE FUNCTION IF USER WANTED GET MORE INFO ABOUT BOT'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*methods_button],resize_keyboard = True)
    await message.reply('Выберите свою опцию', reply = False, reply_markup=keyboard)