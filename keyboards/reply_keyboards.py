from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from catalogues.button_texts import ButtonTexts
from models.users_model import Admin


def main_menu_keyboard(user_id: int = None):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(KeyboardButton(ButtonTexts.Button1))
    if Admin.is_admin(user_id):
        markup.add(KeyboardButton(ButtonTexts.ADMIN_BTN))
    return markup


def back_keyboard(additional_button: str = "") -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if additional_button:
        markup.add(KeyboardButton(additional_button))
    markup.add(KeyboardButton(ButtonTexts.BACK_BUTTON))
    return markup
