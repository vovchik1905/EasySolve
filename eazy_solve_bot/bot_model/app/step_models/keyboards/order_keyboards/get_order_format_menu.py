from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


"""

"""

class GetOrderFormatMenuKeyboard:
    def __init__(self, language: str, order_id: int) -> None:
        self.button_headings = ButtonHeadings(language)

        self.control_btn = InlineKeyboardButton(self.button_headings.CONTROL_FORMAT_HEADING,
                                                            callback_data=ButtonCallbackData.CONTROL_FORMAT_CALLBACK_DATA)

        self.homework_btn = InlineKeyboardButton(self.button_headings.HOMEWORK_FORMAT_HEADING,
                                                            callback_data=ButtonCallbackData.HOMEWORK_FORMAT_CALLBACK_DATA)

        self.exam_btn = InlineKeyboardButton(self.button_headings.EXAM_FORMAT_HEADING,
                                                            callback_data=ButtonCallbackData.EXAM_FORMAT_CALLBACK_DATA)

        self.laba_btn = InlineKeyboardButton(self.button_headings.LABA_FORMAT_HEADING,
                                                            callback_data=ButtonCallbackData.LABA_FORMAT_CALLBACK_DATA)

        self.coursework_btn = InlineKeyboardButton(self.button_headings.COURSEWORK_FORMAT_HEADING,
                                                            callback_data=ButtonCallbackData.COURSEWORK_FORMAT_CALLBACK_DATA)

        self.diploma_btn = InlineKeyboardButton(self.button_headings.DIPLOMA_FORMAT_HEADING,
                                                            callback_data=ButtonCallbackData.DIPLOMA_FORMAT_CALLBACK_DATA)

        self.other_btn = InlineKeyboardButton(self.button_headings.OTHER_FORMAT_HEADING,
                                                            callback_data=ButtonCallbackData.OTHER_FORMAT_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)

        self.order_format_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.order_format_menu_keyboard.add(self.control_btn,
                                            self.homework_btn,
                                            self.exam_btn,
                                            self.laba_btn,
                                            self.coursework_btn,
                                            self.diploma_btn,
                                            self.other_btn)
        self.order_format_menu_keyboard.add(self.back_btn)