from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from filters.callback_filter import my_category
from catalogues.button_texts import ButtonTexts


def category_confirm_inline_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(InlineKeyboardButton(text=ButtonTexts.CONFIRM,
                                    callback_data=my_category.new(category=1)
                                    ),
               InlineKeyboardButton(text=ButtonTexts.CANCEL,
                                    callback_data=my_category.new(category=0)
                                    )
               )
    return markup
