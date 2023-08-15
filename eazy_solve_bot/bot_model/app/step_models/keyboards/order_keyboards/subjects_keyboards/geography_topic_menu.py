from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class GeographyTopicMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.geography_topic_btn = InlineKeyboardButton(self.button_headings.GEOGRAPHY_HEADING,
                                                    callback_data=ButtonCallbackData.GEOGRAPHY_CALLBACK_DATA)

        
        self.geography_topic_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.geography_topic_menu_keyboard.add(self.geography_topic_btn)