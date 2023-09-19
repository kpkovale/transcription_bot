from telebot.types import Message
from telebot import TeleBot
from catalogues.message_texts import MessageTexts
from telebot.async_telebot import AsyncTeleBot
import time
from telebot.asyncio_handler_backends import BaseMiddleware, CancelUpdate


class AntiSpamMiddleware(BaseMiddleware):

    def __init__(self, limit: int, bot: AsyncTeleBot) -> None:
        super().__init__()
        self.last_time = {}
        self.limit = limit
        self.update_types = ['message']
        self.bot = bot

    async def pre_process(self, message, data):
        if not message.from_user.id in self.last_time:
            # User is not in a dict, add user and exit function
            self.last_time[message.from_user.id] = message.date
            return
        if message.date - self.last_time[message.from_user.id] < self.limit:
            # User is flooding
            await self.bot.send_message(message.chat.id, MessageTexts.FLOOD_MESSAGE)
            return CancelUpdate()
        self.last_time[message.from_user.id] = message.date

    async def post_process(self, message, data, exception):
        pass