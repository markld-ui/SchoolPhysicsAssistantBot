from aiogram import types
from loader import dp


@dp.message_handler(lambda message: message.text == 'Нет')
async def disagree(message: types.Message):
    array_disagree = [
                        'Кем разработан этот проект?',
                        'Спасибо, можем приступать.'
                     ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_disagree)
    await message.reply('Что бы вы хотели узнать ещё?',
        reply = False,
        reply_markup = keyboard)