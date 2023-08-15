from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class AdminMainMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.control_panel_btn = InlineKeyboardButton(self.button_headings.CONTROL_PANEL_HEADING,
                                                    callback_data=ButtonCallbackData.ADMIN_CONTROL_PANEL_CALLBACK_DATA)

        self.custom_menu_btn = InlineKeyboardButton(self.button_headings.CUSTOM_MENU_HEADING,
                                                    callback_data=ButtonCallbackData.CUSTOM_MENU_CALLBACK_DATA)
        
        self.admin_main_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.admin_main_menu_keyboard.add(self.control_panel_btn)
        self.admin_main_menu_keyboard.add(self.custom_menu_btn)