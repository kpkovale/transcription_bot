from telebot.asyncio_filters import AdvancedCustomFilter
from telebot.types import Message

class IsButtonFilter(AdvancedCustomFilter):
    key = 'is_button'

    @staticmethod
    async def check(message: Message, values):
        return message.text in values

