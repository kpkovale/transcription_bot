from telebot.async_telebot import AsyncTeleBot as TeleBot
from telebot.types import Message, MessageEntity
from utils.bot_logger import logger
from catalogues.message_texts import MessageTexts
from utils.ya_transcription_api import VoiceMsgRecognizer
from requests import get
from bot_config import TOKEN
from handlers.handler_utils import get_message_link


async def audio_message_transcript_handler(message: Message, bot: TeleBot):
    if not message.voice:
        logger.error("empty voice file")
        return
    await bot.send_chat_action(message.chat.id, "typing", timeout=5)
    file_details = await bot.get_file(message.voice.file_id)
    file = get(f"https://api.telegram.org/file/bot{TOKEN}/{file_details.file_path}").content
    recognizer = VoiceMsgRecognizer()
    # with open(file) as file:
    transcription = recognizer.recognize(file)
    msg_link = get_message_link(message.chat.id, message.message_id)
    reply_id = message.id
    if msg_link:
        reply_id = None
    else:
        msg_link = ""
    if message.from_user.username:
        user_link = f"@{message.from_user.username}"
    else:
        user_link = f"[{message.from_user.full_name}](t.me/{message.from_user.id})"
    await bot.send_message(message.chat.id,
                           msg_link
                           + MessageTexts.BOT_RECOGNITION_MESSAGE.format(user_link, transcription),
                           reply_to_message_id=reply_id
                           )

