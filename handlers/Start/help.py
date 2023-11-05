from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandHelp
from handlers.HelperClient.ClassTypes.choice_method import methods_button
from loader import dp


@dp.message_handler(CommandHelp())
async def help(message : types.Message): # help function user
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*methods_button)
    await message.reply(
        text =
        '''
Мои команды:
    - /help
    - /start

Нажмите на одну из кнопок, чтобы перейти к выбору метода образования
        ''',
        reply = False,
        parse_mode = 'HTML',
        reply_markup=keyboard
        )