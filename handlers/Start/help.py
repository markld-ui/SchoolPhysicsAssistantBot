from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def help(message : types.Message): # help function user
	await message.reply(
        text =
        '''
Мои команды:
    - /help
    - /start
        ''',
        reply = False,
        parse_mode = 'HTML'
        )