from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class GetDurationMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        self.order_1duration_btn = InlineKeyboardButton(self.button_headings.ORDER_1DURATION_HEADING,
                                                        callback_data=ButtonCallbackData.ORDER_1DURATION_CALLBACK_DATA)
        self.order_2duration_btn = InlineKeyboardButton(self.button_headings.ORDER_2DURATION_HEADING,
                                                        callback_data=ButtonCallbackData.ORDER_2DURATION_CALLBACK_DATA)
        self.order_3duration_btn = InlineKeyboardButton(self.button_headings.ORDER_3DURATION_HEADING,
                                                        callback_data=ButtonCallbackData.ORDER_3DURATION_CALLBACK_DATA)
        self.order_4duration_btn = InlineKeyboardButton(self.button_headings.ORDER_4DURATION_HEADING,
                                                        callback_data=ButtonCallbackData.ORDER_4DURATION_CALLBACK_DATA)
        self.order_5duration_btn = InlineKeyboardButton(self.button_headings.ORDER_5DURATION_HEADING,
                                                        callback_data=ButtonCallbackData.ORDER_5DURATION_CALLBACK_DATA)
        self.order_6duration_btn = InlineKeyboardButton(self.button_headings.ORDER_6DURATION_HEADING,
                                                        callback_data=ButtonCallbackData.ORDER_6DURATION_CALLBACK_DATA)
        self.order_7duration_btn = InlineKeyboardButton(self.button_headings.ORDER_7DURATION_HEADING,
                                                        callback_data=ButtonCallbackData.ORDER_7DURATION_CALLBACK_DATA)
        self.order_8duration_btn = InlineKeyboardButton(self.button_headings.ORDER_8DURATION_HEADING,
                                                        callback_data=ButtonCallbackData.ORDER_8DURATION_CALLBACK_DATA)
        self.duration_menu_keyboard = InlineKeyboardMarkup(row_width=4)
        self.duration_menu_keyboard.add(self.order_1duration_btn,
                                        self.order_2duration_btn,
                                        self.order_3duration_btn,
                                        self.order_4duration_btn,
                                        self.order_5duration_btn,
                                        self.order_6duration_btn,
                                        self.order_7duration_btn,
                                        self.order_8duration_btn)