from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def help(message : types.Message): # help function user
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    frist_buttons = ['/start']
    keyboard.add(*frist_buttons)
    await message.reply(
        text =
        '''
Мои команды:
    - /help
    - /start

Нажмите на кнопку, чтобы выйти в главное меню
        ''',
        reply = False,
        parse_mode = 'HTML',
        reply_markup=keyboard
        )