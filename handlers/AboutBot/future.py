from aiogram import types

from loader import dp

@dp.message_handler(lambda message: message.text == 'Планируется добавление формул для 10-11 классов?')
async def future(message: types.Message):
    array_disagree = [
                        'Да',
                        'Нет'
                     ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_disagree)
    await message.reply('В ближайшие 2 года, добавление формул для десятых и одинадцатых классов не планируется. Но, возможно в будущем это будет реализовано.',
        reply = False)
    await message.reply('Перейдём к выбору класса?',
        reply = False,
        reply_markup = keyboard)