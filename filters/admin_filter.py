import telebot.types
from telebot.asyncio_filters import SimpleCustomFilter
from models.users_model import Admin


class AdminFilter(SimpleCustomFilter):
    """
    Filter for admin users
    """
    key = 'admin'

    async def check(self, message: telebot.types.Message):
        if isinstance(message, telebot.types.Message):
            return Admin.is_admin(message.chat.id)