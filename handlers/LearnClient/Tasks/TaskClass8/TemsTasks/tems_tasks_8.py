from aiogram import types
from aiogram.types import FSInputFile

from loader import dp, bot

from handlers.LearnClient.Tasks.choise_class_by_tasks import class_button
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == '8.1t')
async def send_presentation_for_first_theme(message: types.Message):
    await message.answer('Задачи на тему "Тепловые явления"')
    document = FSInputFile(path='utils\\media\\Tasks\\8class\\8.1\\tasks8_1.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '8.2t')
async def send_presentation_for_second_theme(message: types.Message):
    await message.answer('Задачи на тему "Электрические явления"')
    document = FSInputFile(path='utils\\media\\Tasks\\8class\\8.2\\tasks8_2.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '8.3t')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Задачи на тему "Электромагнитные явления"')
    document = FSInputFile(path='utils\\media\\Tasks\\8class\\8.3\\tasks8_3.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '8.4t')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Задачи на тему "Световые явления"')
    document = FSInputFile(path='utils\\media\\Tasks\\8class\\8.4\\tasks8_4.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == 'Выход к выбору T-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button], resize_keyboard=True)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)