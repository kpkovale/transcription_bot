# register filters here or in different folders.

from telebot.async_telebot import AsyncTeleBot
from .callback_filter import *
from .button_filter import IsButtonFilter
from .admin_filter import AdminFilter
from telebot.asyncio_filters import IsReplyFilter, StateFilter
from utils.bot_logger import logger
from bot_config import LOG_LEVEL


def bind_custom_filters(bot: AsyncTeleBot):
    logger.log(LOG_LEVEL, "Registering filters")


    bot.add_custom_filter(AdminFilter())
    bot.add_custom_filter(IsButtonFilter())

    bot.add_custom_filter(MyCategoryCallbackFilter())

    bot.add_custom_filter(IsReplyFilter())
    bot.add_custom_filter(StateFilter(bot))
