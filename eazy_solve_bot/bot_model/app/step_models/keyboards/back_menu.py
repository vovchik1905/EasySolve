from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData, ButtonURLData


class BackMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        
        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                    callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        self.back_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.back_menu_keyboard.add(self.back_btn)