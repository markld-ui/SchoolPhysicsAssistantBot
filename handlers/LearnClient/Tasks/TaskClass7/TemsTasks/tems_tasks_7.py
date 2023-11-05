from aiogram import types
from aiogram.types import FSInputFile

from loader import dp, bot

from handlers.LearnClient.Tasks.choise_class_by_tasks import class_button
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == '7.1t')
async def send_presentation_for_first_theme(message: types.Message):
    await message.answer('Задачи на тему "Взаимодействие тел"')
    document = FSInputFile(path='utils\\media\\Tasks\\7class\\7.1\\tasks7_1.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '7.2t')
async def send_presentation_for_second_theme(message: types.Message):
    await message.answer('Задачи на тему "Давление твёрдых тел, жидкостей и газов"')
    document = FSInputFile(path='utils\\media\\Tasks\\7class\\7.2\\tasks7_2.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '7.3t')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Задачи на тему "Работа, энергия, мощность"')
    document = FSInputFile(path='utils\\media\\Tasks\\7class\\7.3\\tasks7_3.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == 'Выход к выбору T-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button], resize_keyboard=True)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)