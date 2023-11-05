from aiogram.types import Message,ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram import Router

router = Router()

frist_buttons = [
    [KeyboardButton(text='Да, конечно')],
    [KeyboardButton(text='Расскажи о себе')],
]


@router.message(CommandStart())
async def start(message : Message): #function to start bot with buttons
	keyboard = ReplyKeyboardMarkup(keyboard=[*frist_buttons],resize_keyboard=True)
	await message.reply('Привет!\n'
                        'Я твой персональный бот-помощник по физике.\n'
                        'Начнём?',
                        reply = False,
                        reply_markup=keyboard
                        )