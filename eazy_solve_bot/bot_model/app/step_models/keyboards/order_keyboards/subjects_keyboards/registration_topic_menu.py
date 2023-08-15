from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class RegistrationTopicMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.registration_topic_btn = InlineKeyboardButton(self.button_headings.REGISTRATION_HEADING,
                                                    callback_data=ButtonCallbackData.REGISTRATION_CALLBACK_DATA)

        
        self.registration_topic_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.registration_topic_menu_keyboard.add(self.registration_topic_btn)