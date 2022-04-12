from aiogram import types

from loader import dp
from handlers.HelperClient.ClassTypes.choice_method import methods_button

@dp.message_handler(lambda message: message.text == 'Да')
async def agree(message: types.Message):
    '''AGREE FUNCTION IF USER WANTED GET MORE INFO ABOUT BOT'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*methods_button)
    await message.reply('Выберите свою опцию', reply = False, reply_markup=keyboard)