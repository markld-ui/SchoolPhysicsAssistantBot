from aiogram import types
from aiogram.types import FSInputFile

from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from loader import dp, bot

from handlers.LearnClient.Tasks.choise_class_by_tasks import class_button


@dp.message(lambda message: message.text == '11.1t')
async def send_presentation_for_first_theme(message: types.Message):
    await message.answer('Задачи на тему "Механика"')
    document = FSInputFile(path='utils\\media\\Tasks\\11class\\11.1\\tasks11_1.txt')
    await bot.send_document(message.chat.id, document = document)


@dp.message(lambda message: message.text == '11.2t')
async def send_presentation_for_second_theme(message: types.Message):
    await message.answer('Задачи на тему "Молекулярная физика"')
    document = FSInputFile(path='utils\\media\\Tasks\\11class\\11.2\\tasks11_2.txt')
    await bot.send_document(message.chat.id, document = document)



@dp.message(lambda message: message.text == 'Выход к выбору T-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button], resize_keyboard=True)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)