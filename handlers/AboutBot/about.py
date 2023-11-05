from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@dp.message(lambda message: message.text == 'Расскажи о себе')
async def question_by_user(message : types.Message):
    '''---FUNCTION ABOUT BOT OPPORTUNITIES---'''
    agree = [
        [KeyboardButton(text='Да')],
        [KeyboardButton(text='Нет')]
        ]
    keyboard = ReplyKeyboardMarkup(keyboard=[*agree],resize_keyboard = True)
    await message.reply(
'Я Ваш персональный помощник по физике.\n'
'Я направлен на аудиторию обучающихся 7 - 11 классов.\n'
'У меня Вы найдётё формулы, нужные именно для вашего класса.\n'
'А также, у меня Вы можете пройти тему по предоставленному материалу.',
        reply = False)
    await message.reply('Перейдём к выбору опции?',
        reply = False,
        reply_markup = keyboard)