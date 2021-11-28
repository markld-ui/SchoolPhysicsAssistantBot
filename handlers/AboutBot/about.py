from aiogram import types

from loader import dp


'''---ABOUT BOT---'''

@dp.message_handler(lambda message: message.text == 'Расскажи о себе')
async def question_by_user(message : types.Message): #Функция, рассказывающая о возможностях бота
    agree = ['Да', 'Нет']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*agree)
    await message.reply(
'Я Ваш персональный помощник по физике.\n'
'Я направлен на аудиторию обучающихся 7 - 9 классов.\n'
'У меня Вы найдётё формулы, нужные именно для вашего класса,'
' а также, некоторые физические термины и их определения.\n',
        reply = False)
    await message.reply('Перейдём к выбору класса?',
        reply = False,
        reply_markup = keyboard)