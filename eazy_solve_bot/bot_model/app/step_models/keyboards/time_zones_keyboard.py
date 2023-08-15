from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class TimeZoneKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.time_zone_utc_minus12_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS12,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS12_CALLBACK_DATA)
        
        self.time_zone_utc_minus11_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS11,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS11_CALLBACK_DATA)
        
        self.time_zone_utc_minus10_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS10,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS10_CALLBACK_DATA)

        self.time_zone_utc_minus09_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS09,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS09_CALLBACK_DATA)

        self.time_zone_utc_minus08_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS08,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS08_CALLBACK_DATA)

        self.time_zone_utc_minus07_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS07,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS07_CALLBACK_DATA)

        self.time_zone_utc_minus06_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS06,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS06_CALLBACK_DATA)

        self.time_zone_utc_minus05_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS05,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS05_CALLBACK_DATA)

        self.time_zone_utc_minus04_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS04,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS04_CALLBACK_DATA)

        self.time_zone_utc_minus03_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS03,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS03_CALLBACK_DATA)

        self.time_zone_utc_minus02_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS02,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS02_CALLBACK_DATA)

        self.time_zone_utc_minus01_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_MINUS01,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_MINUS01_CALLBACK_DATA)

        self.time_zone_utc_plus00_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS00,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS00_CALLBACK_DATA)

        self.time_zone_utc_plus01_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS01,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS01_CALLBACK_DATA)

        self.time_zone_utc_plus02_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS02,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS02_CALLBACK_DATA)

        self.time_zone_utc_plus03_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS03,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS03_CALLBACK_DATA)

        self.time_zone_utc_plus04_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS04,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS04_CALLBACK_DATA)

        self.time_zone_utc_plus05_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS05,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS05_CALLBACK_DATA)

        self.time_zone_utc_plus06_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS06,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS06_CALLBACK_DATA)

        self.time_zone_utc_plus07_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS07,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS07_CALLBACK_DATA)

        self.time_zone_utc_plus08_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS08,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS08_CALLBACK_DATA)

        self.time_zone_utc_plus09_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS09,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS09_CALLBACK_DATA)

        self.time_zone_utc_plus10_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS10,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS10_CALLBACK_DATA)

        self.time_zone_utc_plus11_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS11,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS11_CALLBACK_DATA)

        self.time_zone_utc_plus12_btn = InlineKeyboardButton(self.button_headings.TIME_ZONE_UTC_PLUS12,
                                                    callback_data=ButtonCallbackData.TIME_ZONE_UTC_PLUS12_CALLBACK_DATA)


        
        self.time_zone_keyboard = InlineKeyboardMarkup(row_width=4)
        self.time_zone_keyboard.add(self.time_zone_utc_minus12_btn, self.time_zone_utc_minus11_btn,
                                    self.time_zone_utc_minus10_btn, self.time_zone_utc_minus09_btn,
                                    self.time_zone_utc_minus08_btn, self.time_zone_utc_minus07_btn,
                                    self.time_zone_utc_minus06_btn, self.time_zone_utc_minus05_btn,
                                    self.time_zone_utc_minus04_btn, self.time_zone_utc_minus03_btn,
                                    self.time_zone_utc_minus02_btn, self.time_zone_utc_minus01_btn,
                                    self.time_zone_utc_plus00_btn, self.time_zone_utc_plus01_btn,
                                    self.time_zone_utc_plus02_btn, self.time_zone_utc_plus03_btn,
                                    self.time_zone_utc_plus04_btn, self.time_zone_utc_plus05_btn,
                                    self.time_zone_utc_plus06_btn, self.time_zone_utc_plus07_btn,
                                    self.time_zone_utc_plus08_btn, self.time_zone_utc_plus09_btn,
                                    self.time_zone_utc_plus10_btn, self.time_zone_utc_plus11_btn,
                                    self.time_zone_utc_plus12_btn)
        