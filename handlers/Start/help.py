from aiogram import types 

from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


'''---HELP COMMAND---'''

@dp.message_handler(CommandHelp())
async def help(message : types.Message):
	await message.reply(
        text =
        '''
Мои команды:
    - /help
    - unknow now command
    - unknow now command
    - unknow now command
        ''',
        reply = False,
        parse_mode = 'HTML'
        )
