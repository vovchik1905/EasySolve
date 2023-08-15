from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class GetTimeMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        self.deadline_time_btn = InlineKeyboardButton(self.button_headings.GET_ORDER_TIME_HEADING,
                                                    callback_data=ButtonCallbackData.GET_ORDER_TIME_CALLBACK_DATA)
        self.get_time_menu_keyboard = InlineKeyboardMarkup()
        self.get_time_menu_keyboard.add(self.deadline_time_btn)