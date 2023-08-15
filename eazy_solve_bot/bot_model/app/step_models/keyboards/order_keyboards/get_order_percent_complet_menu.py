from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class GetOrderPercentCompleteMenuKeyboard:
    def __init__(self, language: str, order_id: int) -> None:
        self.button_headings = ButtonHeadings(language)
        
        self.ten_percent_btn = InlineKeyboardButton(self.button_headings.TEN_PERCENT_HEADING,
                                                    callback_data=ButtonCallbackData.TEN_PERCENT_CALLBACK_DATA)

        self.twenty_percent_btn = InlineKeyboardButton(self.button_headings.TWENTY_PERCENT_HEADING,
                                                        callback_data=ButtonCallbackData.TWENTY_PERCENT_CALLBACK_DATA)

        self.thirty_percent_btn = InlineKeyboardButton(self.button_headings.THIRTY_PERCENT_HEADING,
                                                        callback_data=ButtonCallbackData.THIRTY_PERCENT_CALLBACK_DATA)

        self.forty_percent_btn = InlineKeyboardButton(self.button_headings.FORTY_PERCENT_HEADING,
                                                        callback_data=ButtonCallbackData.FORTY_PERCENT_CALLBACK_DATA)

        self.fifty_percent_btn = InlineKeyboardButton(self.button_headings.FIFTY_PERCENT_HEADING,
                                                            callback_data=ButtonCallbackData.FIFTY_PERCENT_CALLBACK_DATA)

        self.sixty_percent_btn = InlineKeyboardButton(self.button_headings.SIXTY_PERCENT_HEADING,
                                                            callback_data=ButtonCallbackData.SIXTY_PERCENT_CALLBACK_DATA)

        self.seventy_percent_btn = InlineKeyboardButton(self.button_headings.SEVENTY_PERCENT_HEADING,
                                                            callback_data=ButtonCallbackData.SEVENTY_PERCENT_CALLBACK_DATA)

        self.eighty_percent_btn = InlineKeyboardButton(self.button_headings.EIGHTY_PERCENT_HEADING,
                                                            callback_data=ButtonCallbackData.EIGHTY_PERCENT_CALLBACK_DATA)

        self.ninety_percent_btn = InlineKeyboardButton(self.button_headings.NINETY_PERCENT_HEADING,
                                                            callback_data=ButtonCallbackData.NINETY_PERCENT_CALLBACK_DATA)

        self.hundred_percent_btn = InlineKeyboardButton(self.button_headings.HUNDRED_PERCENT_HEADING,
                                                            callback_data=ButtonCallbackData.HUNDRED_PERCENT_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)

        self.get_order_percent_menu_keyboard = InlineKeyboardMarkup(row_width=5)
        self.get_order_percent_menu_keyboard.add(self.ten_percent_btn,
                                                    self.twenty_percent_btn,
                                                    self.thirty_percent_btn,
                                                    self.forty_percent_btn,
                                                    self.fifty_percent_btn,
                                                    self.sixty_percent_btn,
                                                    self.seventy_percent_btn,
                                                    self.eighty_percent_btn,
                                                    self.ninety_percent_btn,
                                                    self.hundred_percent_btn)
        self.get_order_percent_menu_keyboard.add(self.back_btn)