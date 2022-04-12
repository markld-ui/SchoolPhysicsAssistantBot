from aiogram import types
from loader import dp


@dp.message_handler(lambda message: message.text == 'Расскажи о себе')
async def question_by_user(message : types.Message):
    '''---FUNCTION ABOUT BOT OPPORTUNITIES---'''
    agree = ['Да', 'Нет']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*agree)
    await message.reply(
'Я Ваш персональный помощник по физике.\n'
'Я направлен на аудиторию обучающихся 7 - 11 классов.\n'
'У меня Вы найдётё формулы, нужные именно для вашего класса.\n'
'А также, у меня Вы можете пройти тему по предоставленному материалу.',
        reply = False)
    await message.reply('Перейдём к выбору опции?',
        reply = False,
        reply_markup = keyboard)