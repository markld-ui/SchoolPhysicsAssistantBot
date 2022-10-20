from aiogram import types

from loader import dp


choice_tems_eleven_class = [
		'11.1t',
		'11.2t',
		'Выход к выбору T-класса'
]


@dp.message_handler(lambda message: message.text == '11t')
async def isPresForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_eleven_class)
	
	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n11.1 - Электродинамика за 11 класс\n11.2 - Физика высоких энергий', reply=False, reply_markup=keyboard)