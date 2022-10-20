from aiogram import types

from loader import dp


choice_tems_eight_class = [
		'11.1p',
		'11.2p',
		'Выход к выбору P-класса'
]


@dp.message_handler(lambda message: message.text == '11p')
async def isPresForEight(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_eight_class)
	
	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n11.1 - Электродинамика за 11 класс\n11.2 - Физика высоких энергий', reply=False, reply_markup=keyboard)