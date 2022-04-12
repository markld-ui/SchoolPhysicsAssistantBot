from aiogram import types
from handlers.HelperClient.ClassTypes.choice_method import methods_button
from loader import dp


@dp.message_handler(lambda message: message.text == 'Выйти к выбору операции')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*methods_button)
    await message.reply(
    'Выберите нужную для Вас функцию:',
    reply = False,
    reply_markup = keyboard
    )