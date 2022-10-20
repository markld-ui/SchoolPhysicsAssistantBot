from aiogram import types

from loader import dp

arrayWithThemes = ['10.1v', '10.2v', '10.3v', 'Выйти к выбору V-класса']

@dp.message_handler(lambda message: message.text == '10v')
async def isVideoForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
	keyboard.add(*arrayWithThemes)
	await message.reply('Выберите тему, для которой хотите получить видео:', reply=False)
	await message.reply('Темы:\n10.1 - Механика\n10.2 - Молекулярная физика\n10.3 - Электродинамика за 10 класс', reply=False, reply_markup=keyboard)