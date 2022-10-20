from aiogram import types
from loader import dp
from handlers.HelperClient.ClassTypes.Handbook.class10 import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot


@dp.message_handler(lambda message: message.text == '10.1')
async def formuls(message : types.Message):
    '''function for 10.1 theme'''
    media = types.MediaGroup()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Выми выбрана тема "Механика". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media.attach_photo(types.InputFile('utils\\media\\image\\10class\\mechanicap1.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\10class\\mechanicap2.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\10class\\mechanicap3.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\10class\\mechanicap4.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\10class\\mechanicap5.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\10class\\mechanicap6.jpg'))
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler(lambda message: message.text == '10.2')
async def formuls(message : types.Message):
    '''function for 10.2 theme'''
    media = types.MediaGroup()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Молекулярная физика". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media.attach_photo(types.InputFile('utils\\media\\image\\10class\\moleculyarnayap1.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\10class\\moleculyarnayap2.jpg'))
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler(lambda message: message.text == '10.3')
async def formuls(message : types.Message):
    '''function for 10.2 theme'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Электродинамика за 10 класс". Пожалуйста:',
    reply = False,
    reply_markup = keyboard)
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\media\\image\\10class\\electrodinamica.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )