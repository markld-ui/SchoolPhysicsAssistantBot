from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@dp.message(lambda message: message.text == 'Кем разработан этот проект?')
async def disagree(message: types.Message):
    array_disagree = [
        [KeyboardButton(text='Да')],
        [KeyboardButton(text='Нет')]
        ]
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_disagree],resize_keyboard = True)
    await message.reply('Этот проект находится в стадии разработки. Пока что над ним работает бывший ученик МАОУ СОШ 197 г. Екатеринбург 11 класса и нынешний студент ТУСУРа',
        reply = False)
    await message.reply('Перейдём к выбору опции?',
        reply = False,
        reply_markup = keyboard)