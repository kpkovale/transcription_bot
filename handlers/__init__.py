# register your project handlers here
from telebot.async_telebot import AsyncTeleBot
from .any_text import any_text_handler
from .audio_handlers import audio_message_transcript_handler


def register_custom_handlers(bot: AsyncTeleBot):
    # register your handlers or handlers collectors from subfolders here
    bot.register_message_handler(audio_message_transcript_handler, content_types=['voice'], pass_bot=True)
    bot.register_message_handler(any_text_handler, content_types=['text'], pass_bot=True)
