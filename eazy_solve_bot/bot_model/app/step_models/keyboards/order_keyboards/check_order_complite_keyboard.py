from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData

class CheckOrderCompliteMenu:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        
        self.yes_btn = InlineKeyboardButton(self.button_headings.YES_BUTTON_HEADING,
                                                    callback_data=ButtonCallbackData.TRUE_CHECK_ORDER_COMPLITE_TO_SEND_MENU_CALLBACK_DATA)
        
        self.no_btn = InlineKeyboardButton(self.button_headings.NO_BUTTON_HEADING,
                                                    callback_data=ButtonCallbackData.FALSE_CHECK_ORDER_COMPLITE_TO_SEND_MENU_CALLBACK_DATA)
        
        self.check_order_complite_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.check_order_complite_menu_keyboard.add(self.yes_btn)