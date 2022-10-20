from aiogram import types
from handlers.LearnClient.choice_means import types_button
from loader import dp


@dp.message_handler(lambda message: message.text == 'Выйти к выбору способов')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*types_button)
    await message.reply(
    'Выберите нужный для Вас способ образования:',
    reply = False,
    reply_markup = keyboard
    )