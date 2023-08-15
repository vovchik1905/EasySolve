from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData

class BinCheckAnswerMenu:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        self.yes_button_btn = InlineKeyboardButton(self.button_headings.YES_BUTTON_HEADING,
                                                    callback_data=ButtonCallbackData.YES_BUTTON_CALLBACK_DATA)

        self.no_button_btn = InlineKeyboardButton(self.button_headings.NO_BUTTON_HEADING,
                                                    callback_data=ButtonCallbackData.NO_BUTTON_CALLBACK_DATA)
        
        self.bin_check_answer_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.bin_check_answer_menu_keyboard.add(self.yes_button_btn)
        self.bin_check_answer_menu_keyboard.add(self.no_button_btn)