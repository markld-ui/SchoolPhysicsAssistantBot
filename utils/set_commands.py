from aiogram import types

async def bot_commands(dp):
	await dp.bot.set_my_commands(

		[
			types.BotCommand('help', 'Показать справку команд'),
			types.BotCommand('start', 'Запустить бота')
		]

	)