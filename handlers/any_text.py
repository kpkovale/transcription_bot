from telebot.async_telebot import AsyncTeleBot as TeleBot
from telebot.types import Message
from utils.bot_logger import logger
from bot_config import LOG_LEVEL
from telebot.asyncio_handler_backends import ContinueHandling


async def any_text_handler(message: Message, bot: TeleBot):
    logger.log(LOG_LEVEL, f"chat / message: {message.chat.id} / {message.id}, {message.from_user.full_name}: "
                          f"'{message.text}'")
    return ContinueHandling()
