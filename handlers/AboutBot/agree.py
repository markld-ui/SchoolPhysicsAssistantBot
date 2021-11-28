from aiogram import types

from loader import dp
from handlers.ClassTypes.choice_class import class_button

@dp.message_handler(lambda message: message.text == 'Да')
async def agree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply = False, reply_markup=keyboard)