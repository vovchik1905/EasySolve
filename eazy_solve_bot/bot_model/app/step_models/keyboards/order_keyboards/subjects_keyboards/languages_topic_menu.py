from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


RUSSIAN = "RUSSIAN"
CHINESE = "CHINESE"
ENGLISH = "ENGLISH"
FRENCH = "FRENCH"
GERMAN = "GERMAN"
SPANISH = "SPANISH"
OTHER_LANGUAGES = "OTHER_LANGUAGES"

class LanguagesTopicMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.russian_topic_btn = InlineKeyboardButton(self.button_headings.RUSSIAN_HEADING,
                                                    callback_data=ButtonCallbackData.RUSSIAN_CALLBACK_DATA)
        
        self.english_topic_btn = InlineKeyboardButton(self.button_headings.ENGLISH_HEADING,
                                                    callback_data=ButtonCallbackData.ENGLISH_CALLBACK_DATA)

        self.chinese_topic_btn = InlineKeyboardButton(self.button_headings.CHINESE_HEADING,
                                                    callback_data=ButtonCallbackData.CHINESE_CALLBACK_DATA)

        self.french_topic_btn = InlineKeyboardButton(self.button_headings.FRENCH_HEADING,
                                                    callback_data=ButtonCallbackData.FRENCH_CALLBACK_DATA)

        self.german_topic_btn = InlineKeyboardButton(self.button_headings.GERMAN_HEADING,
                                                    callback_data=ButtonCallbackData.GERMAN_CALLBACK_DATA)
        
        self.spanish_topic_btn = InlineKeyboardButton(self.button_headings.SPANISH_HEADING,
                                                    callback_data=ButtonCallbackData.SPANISH_CALLBACK_DATA)

        self.other_languages_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_LANGUAGES_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_LANGUAGES_CALLBACK_DATA)

        
        self.languages_topic_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.languages_topic_menu_keyboard.add(self.russian_topic_btn, self.english_topic_btn,
                                                self.chinese_topic_btn, self.french_topic_btn, 
                                                self.german_topic_btn, self.spanish_topic_btn,
                                                self.other_languages_topic_btn)