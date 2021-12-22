from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def start(message : types.Message): #function to start bot with buttons
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	frist_buttons = ['Да, конечно', 'Расскажи о себе']
	keyboard.add(*frist_buttons)
	await message.reply('Привет!\n'
                        'Я твой персональный бот-помощник по физике.\n'
                        'Начнём?',
                        reply = False,
                        reply_markup=keyboard
                        )