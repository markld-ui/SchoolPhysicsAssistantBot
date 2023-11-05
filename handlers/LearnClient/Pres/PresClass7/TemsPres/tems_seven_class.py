from aiogram import types
from aiogram.types import FSInputFile

from loader import dp, bot
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup

from handlers.LearnClient.Pres.choise_class_by_pres import class_button


@dp.message(lambda message: message.text == '7.1p')
async def send_presentation_for_first_theme(message: types.Message):
    await message.answer('Презентация на тему "Взаимодействие тел"')
    document = FSInputFile(path='utils\\media\\Presentations\\7class\\7.1\\pres1.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '7.2p')
async def send_presentation_for_second_theme(message: types.Message):
    await message.answer('Презентация на тему "Давление твёрдых тел, жидкостей и газов"')
    document = FSInputFile(path='utils\\media\\Presentations\\7class\\7.2\\pres2.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '7.3p')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Презентация на тему "Работа, энергия, мощность"')
    document = FSInputFile(path='utils\\media\\Presentations\\7class\\7.3\\pres3.txt')
    await bot.send_document(message.chat.id, document = document)

@dp.message(lambda message: message.text == 'Выход к выбору P-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button], resize_keyboard=True)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)