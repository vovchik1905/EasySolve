from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData, ButtonURLData


class BalanceMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        
        self.cash_in_btn = InlineKeyboardButton(self.button_headings.CASH_IN_HEADING,
                                                    callback_data=ButtonCallbackData.CASH_IN_CALLBACK_DATA)

        self.cash_out_btn = InlineKeyboardButton(self.button_headings.CASH_OUT_HEADING,
                                                    callback_data=ButtonCallbackData.CASH_OUT_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                    callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        self.balance_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.balance_menu_keyboard.add(self.cash_in_btn, self.cash_out_btn)
        self.balance_menu_keyboard.add(self.back_btn)