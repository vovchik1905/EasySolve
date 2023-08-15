from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class OrderImportanceMenuKeyboard:
    def __init__(self, language: str, user_id: int) -> None:
        self.button_headings = ButtonHeadings(language)

        self.standart_importance_btn = InlineKeyboardButton(self.button_headings.STANDART_IMPORTANCE_HEADING,
                                                    callback_data=ButtonCallbackData.STANDART_IMPORTANCE_CALLBACK_DATA)

        self.now_importance_btn = InlineKeyboardButton(self.button_headings.NOW_IMPORTANCE_HEADING,
                                                    callback_data=ButtonCallbackData.NOW_IMPORTANCE_CALLBACK_DATA)

        self.important_importance_btn = InlineKeyboardButton(self.button_headings.IMPORTANT_IMPORTANCE_HEADING,
                                                    callback_data=ButtonCallbackData.IMPORTANT_IMPORTANCE_CALLBACK_DATA)

        self.voluminous_importance_btn = InlineKeyboardButton(self.button_headings.VOLUMINOUS_IMPORTANCE_HEADING,
                                                    callback_data=ButtonCallbackData.VOLUMINOUS_IMPORTANCE_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        self.order_importance_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.order_importance_menu_keyboard.add(self.standart_importance_btn)
        self.order_importance_menu_keyboard.add(self.now_importance_btn)
        self.order_importance_menu_keyboard.add(self.important_importance_btn)
        self.order_importance_menu_keyboard.add(self.voluminous_importance_btn)
        self.order_importance_menu_keyboard.add(self.back_btn)