from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData, ButtonURLData


class MyProfileMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        
        self.set_banking_details_btn = InlineKeyboardButton(self.button_headings.SET_BANKING_DETAILS_HEADINGS,
                                                    callback_data=ButtonCallbackData.SET_BANKING_DETAILS_CALLBACK_DATA)

        self.set_currency_btn = InlineKeyboardButton(self.button_headings.SET_CURRENCY_HEADINGS,
                                                    callback_data=ButtonCallbackData.SET_CURRENCY_CALLBACK_DATA)

        self.set_language_btn = InlineKeyboardButton(self.button_headings.SET_LANGUAGE_HEADING,
                                                    callback_data=ButtonCallbackData.SET_LANGUAGE_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                    callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        self.my_profile_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.my_profile_menu_keyboard.add(self.set_banking_details_btn)
        self.my_profile_menu_keyboard.add(self.set_currency_btn)
        self.my_profile_menu_keyboard.add(self.set_language_btn)
        self.my_profile_menu_keyboard.add(self.back_btn)