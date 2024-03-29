from aiogram import types
from aiogram.types import FSInputFile

from loader import dp, bot

from handlers.LearnClient.Pres.choise_class_by_pres import class_button
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == '9.1p')
async def send_presentation_for_first_theme(message: types.Message):
    user_id = message.from_user.id
    await message.answer('Презентация на тему "Законы взаимодействия и движения тел"')
    document = FSInputFile(path='utils\\media\\Presentations\\9class\\9.1\\pres1.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '9.2p')
async def send_presentation_for_second_theme(message: types.Message):
    user_id = message.from_user.id
    await message.answer('Презентация на тему "Электромагнитное поле"')
    document = FSInputFile(path='utils\\media\\Presentations\\9class\\9.2\\pres2.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '9.3p')
async def send_presentation_for_third_theme(message: types.Message):
    user_id = message.from_user.id
    await message.answer('Презентация на тему "Строение атома и атомного ядра"')
    document = FSInputFile(path='utils\\media\\Presentations\\9class\\9.3\\pres3.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == 'Выход к выбору P-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button], resize_keyboard=True)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)