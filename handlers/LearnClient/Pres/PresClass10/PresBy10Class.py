from aiogram import types

from loader import dp


choice_tems_eight_class = [
		'10.1p',
		'10.2p',
		'10.3p',
		'Выход к выбору P-класса'
]


@dp.message_handler(lambda message: message.text == '10p')
async def isPresForEight(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_eight_class)
	
	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n10.1 - Механика\n10.2 - Молекулярная физика\n10.3 - Электродинамика за 10 класс', reply=False, reply_markup=keyboard)