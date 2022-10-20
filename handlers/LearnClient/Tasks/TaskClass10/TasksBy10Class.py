from aiogram import types

from loader import dp


choice_tems_ten_class = [
		'10.1t',
		'10.2t',
		'10.3t', 
		'Выход к выбору T-класса'
]


@dp.message_handler(lambda message: message.text == '10t')
async def isPresForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_ten_class)
	
	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n10.1 - Механика\n10.2 - Молекулярная физика\n10.3 - Электродинамика за 10 класс', reply=False, reply_markup=keyboard)