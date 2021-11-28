import logging

from loader import dp
from data.config import ADMINS

async def notify_admin(dp):
	for admin in ADMINS: #Проходимся по списку админов и на каждой итерации пишем в личные сообщение о запуске бота
		try:
			await dp.bot.send_message(text = "Бот был запущен", chat_id = admin)
		except Exception as err:
			logging.exception(err)
