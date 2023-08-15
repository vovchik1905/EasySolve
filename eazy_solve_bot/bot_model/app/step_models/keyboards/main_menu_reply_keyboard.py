from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class MainMenuReplyKeyboard:
    def __init__(self, language: str) -> None:
        self.first_button = KeyboardButton(ButtonHeadings.MAIN_MENU_HEADING)
        self.one_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard = True,)
        
        self.one_menu_keyboard.row(self.first_button)