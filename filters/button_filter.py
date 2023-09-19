from telebot.asyncio_filters import AdvancedCustomFilter


class IsButtonFilter(AdvancedCustomFilter):
    key = 'is_button'

    @staticmethod
    async def check(message, values):
        return message.text in values

