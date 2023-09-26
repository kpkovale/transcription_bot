from telebot.async_telebot import AsyncTeleBot as TeleBot
from telebot.types import Message
from utils.bot_logger import logger
from catalogues.message_texts import MessageTexts
from utils.ya_transcription_api import VoiceMsgRecognizer
from requests import get
from bot_config import TOKEN


async def audio_message_transcript_handler(message: Message, bot: TeleBot):
    if not message.voice:
        logger.error("empty voice file")
        return
    file_details = await bot.get_file(message.voice.file_id)
    file = get(f"https://api.telegram.org/file/bot{TOKEN}/{file_details.file_path}").content
    recognizer = VoiceMsgRecognizer()
    # with open(file) as file:
    transcription = recognizer.recognize(file)
    await bot.send_message(message.chat.id,
                           MessageTexts.BOT_RECOGNITION_MESSAGE.format(transcription),
                           reply_to_message_id=message.id)
