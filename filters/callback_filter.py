from telebot import types
from telebot.asyncio_filters import AdvancedCustomFilter
from telebot.callback_data import CallbackData, CallbackDataFilter

my_category = CallbackData("category", prefix="my_category")


class MyCategoryCallbackFilter(AdvancedCustomFilter):
    key = 'category_config'

    async def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)

