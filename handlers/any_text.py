from telebot.async_telebot import AsyncTeleBot as TeleBot
from telebot.types import Message
from utils.bot_logger import logger
from bot_config import LOG_LEVEL
from catalogues.message_texts import MessageTexts
from keyboards.reply_keyboards import main_menu_keyboard


async def any_text_handler(message: Message, bot: TeleBot):
    logger.log(LOG_LEVEL, f"message: {message.chat.id}, {message.from_user.full_name}: "
                          f"'{message.text}'")
    await bot.send_message(message.chat.id, MessageTexts.MESSAGE_TEMPLATE1,
                           reply_markup=main_menu_keyboard(message.from_user.id))
