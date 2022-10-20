from aiogram import types
from loader import dp, bot
from handlers.LearnClient.Video.TenClass.VideoBy10Class import arrayWithThemes
from handlers.LearnClient.Video.choise_class_by_video import class_button

@dp.message_handler(lambda message: message.text == '10.1v')
async def firstThemeHandler(message: types.Message):
	user_id = message.from_user.id
	media = types.MediaGroup()
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*arrayWithThemes)
	media.attach_video(types.InputFile('utils/media/video/10class/10.1/video.mp4'))
	media.attach_video(types.InputFile('utils/media/video/10class/10.1/video2.mp4'))
	await message.answer('Видео на тему "Механика"')
	await bot.send_chat_action(user_id, types.chat.ChatActions.UPLOAD_VIDEO)
	await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler(lambda message: message.text == '10.2v')
async def secondThemeHandler(message: types.Message):
	user_id = message.from_user.id
	media = types.MediaGroup()
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*arrayWithThemes)
	media.attach_video(types.InputFile('utils/media/video/10class/10.2/video.mp4'))
	media.attach_video(types.InputFile('utils/media/video/10class/10.2/video2.mp4'))
	await message.answer('Видео на тему "Молекулярная физика"')
	await bot.send_chat_action(user_id, types.chat.ChatActions.UPLOAD_VIDEO)
	await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler(lambda message: message.text == '10.3v')
async def thirdThemeHandler(message: types.Message):
	user_id = message.from_user.id
	media = types.MediaGroup()
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*arrayWithThemes)
	media.attach_video(types.InputFile('utils/media/video/10class/10.3/video.mp4'))
	media.attach_video(types.InputFile('utils/media/video/10class/10.3/video2.mp4'))
	await message.answer('Видео на тему "Электродинамика за 10 класс"')
	await bot.send_chat_action(user_id, types.chat.ChatActions.UPLOAD_VIDEO)
	await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler(lambda message: message.text == 'Выйти к выбору V-класса')
async def exitToChoiceVideoClass(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*class_button)
	await message.reply('Выберите класс',reply=False, reply_markup=keyboard)
