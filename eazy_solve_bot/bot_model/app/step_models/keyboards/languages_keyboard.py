from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class LanguagesKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.russian_language_btn = InlineKeyboardButton(self.button_headings.RUSSIAN_LANGUAGE_HEADING,
                                                    callback_data=ButtonCallbackData.RUSSIAN_LANGUAGE_CALLBACK_DATA)
        
        self.chinese_language_btn = InlineKeyboardButton(self.button_headings.CHINESE_LANGUAGE_HEADING,
                                                        callback_data=ButtonCallbackData.CHINESE_LANGUAGE_CALLBACK_DATA)
        
        self.english_language_btn = InlineKeyboardButton(self.button_headings.ENGLISH_LANGUAGE_HEADING,
                                                    callback_data=ButtonCallbackData.ENGLISH_LANGUAGE_CALLBACK_DATA)
        
        self.french_language_btn = InlineKeyboardButton(self.button_headings.FRENCH_LANGUAGE_HEADING,
                                                callback_data=ButtonCallbackData.FRENCH_LANGUAGE_CALLBACK_DATA)
        
        self.german_language_btn = InlineKeyboardButton(self.button_headings.GERMAN_LANGUAGE_HEADING,
                                                callback_data=ButtonCallbackData.GERMAN_LANGUAGE_CALLBACK_DATA)
        
        self.spanish_language_btn = InlineKeyboardButton(self.button_headings.SPANISH_LANGUAGE_HEADING,
                                                callback_data=ButtonCallbackData.SPANISH_LANGUAGE_CALLBACK_DATA)
        
        self.portuguese_language_btn = InlineKeyboardButton(self.button_headings.PORTUGUESE_LANGUAGE_HEADING,
                                                            callback_data=ButtonCallbackData.PORTUGUESE_LANGUAGE_CALLBACK_DATA)
        
        self.ukrainian_language_btn = InlineKeyboardButton(self.button_headings.UKRAINIAN_LANGUAGE_HEADING,
                                                            callback_data=ButtonCallbackData.UKRAINIAN_LANGUAGE_CALLBACK_DATA)

        self.belarusian_language_btn = InlineKeyboardButton(self.button_headings.BELARUSIAN_LANGUAGE_HEADING,
                                                            callback_data=ButtonCallbackData.BELARUSIAN_LANGUAGE_CALLBACK_DATA)

        self.kazakh_language_btn = InlineKeyboardButton(self.button_headings.KAZAKH_LANGUAGE_HEADING,
                                                            callback_data=ButtonCallbackData.KAZAKH_LANGUAGE_CALLBACK_DATA)

        self.georgian_language_btn = InlineKeyboardButton(self.button_headings.GEORGIAN_LANGUAGE_HEADING,
                                                            callback_data=ButtonCallbackData.GEORGIAN_LANGUAGE_CALLBACK_DATA)
        
        self.armenian_language_btn = InlineKeyboardButton(self.button_headings.ARMENIAN_LANGUAGE_HEADING,
                                                            callback_data=ButtonCallbackData.ARMENIAN_LANGUAGE_CALLBACK_DATA)
        
        self.hebrew_language_btn = InlineKeyboardButton(self.button_headings.HEBREW_LANGUAGE_HEADING,
                                                            callback_data=ButtonCallbackData.HEBREW_LANGUAGE_CALLBACK_DATA)

        self.turkish_language_btn = InlineKeyboardButton(self.button_headings.TURKISH_LANGUAGE_HEADING,
                                                            callback_data=ButtonCallbackData.TURKISH_LANGUAGE_CALLBACK_DATA)
        
        self.languages_keyboard = InlineKeyboardMarkup(row_width=2)
        self.languages_keyboard.add(self.russian_language_btn, self.chinese_language_btn)
        self.languages_keyboard.add(self.english_language_btn, self.french_language_btn)
        self.languages_keyboard.add(self.german_language_btn, self.spanish_language_btn)
        self.languages_keyboard.add(self.portuguese_language_btn, self.ukrainian_language_btn)
        self.languages_keyboard.add(self.belarusian_language_btn, self.kazakh_language_btn)
        self.languages_keyboard.add(self.georgian_language_btn, self.armenian_language_btn)
        self.languages_keyboard.add(self.hebrew_language_btn, self.turkish_language_btn)


