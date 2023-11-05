from aiogram import types
from handlers.filters.filters import TextFilter
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


array_choice = [
    [KeyboardButton(text='7.1')],
    [KeyboardButton(text='7.2')],
    [KeyboardButton(text='7.3')],
    [KeyboardButton(text='Выход')],
]

@dp.message(TextFilter('7 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 7 class'''
	keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
	await message.reply('Темы:\n7.1 - Взаимодействие тел\n7.2 - Давление твёрдых тел, жидкостей и газов\n7.3 - Работа, энергия, мощность', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 7 класса:',
		reply = False,
		reply_markup = keyboard)