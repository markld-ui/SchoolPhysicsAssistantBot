from aiogram import types

from loader import dp

arrayWithThemes = ['8.1v', '8.2v', '8.3v', '8.4v', 'Выйти к выбору V-класса']

@dp.message_handler(lambda message: message.text == '8v')
async def isVideoForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
	keyboard.add(*arrayWithThemes)
	await message.reply('Выберите тему, для которой хотите получить видео:', reply=False)
	await message.reply('Темы:\n8.1 - Тепловые явления\n8.2 - Электрические явления\n8.3 - Электромагнитные явления\n8.4 - Световые явления', reply=False, reply_markup=keyboard)