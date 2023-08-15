from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class EconomyMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.logistics_topic_btn = InlineKeyboardButton(self.button_headings.LOGISTICS_HEADING,
                                                    callback_data=ButtonCallbackData.LOGISTICS_CALLBACK_DATA)
        
        self.macroeconomics_topic_btn = InlineKeyboardButton(self.button_headings.MACROECONOMICS_HEADING,
                                                    callback_data=ButtonCallbackData.MACROECONOMICS_CALLBACK_DATA)

        self.marketing_topic_btn = InlineKeyboardButton(self.button_headings.MARKETING_HEADING,
                                                    callback_data=ButtonCallbackData.MARKETING_CALLBACK_DATA)

        self.management_topic_btn = InlineKeyboardButton(self.button_headings.MANAGEMENT_HEADING,
                                                    callback_data=ButtonCallbackData.MANAGEMENT_CALLBACK_DATA)

        self.microeconomics_topic_btn = InlineKeyboardButton(self.button_headings.MICROECONOMICS_HEADING,
                                                    callback_data=ButtonCallbackData.MICROECONOMICS_CALLBACK_DATA)
        
        self.taxarion_topic_btn = InlineKeyboardButton(self.button_headings.TAXATION_HEADING,
                                                    callback_data=ButtonCallbackData.TAXATION_CALLBACK_DATA)

        self.personnel_management_topic_btn = InlineKeyboardButton(self.button_headings.PERSONNEL_MANAGEMENT_HEADING,
                                                    callback_data=ButtonCallbackData.PERSONNEL_MANAGEMENT_CALLBACK_DATA)

        self.economy_topic_btn = InlineKeyboardButton(self.button_headings.ECONOMY_HEADING,
                                                    callback_data=ButtonCallbackData.ECONOMY_CALLBACK_DATA)

        self.accounting_topic_btn = InlineKeyboardButton(self.button_headings.ACCOUNTING_HEADING,
                                                    callback_data=ButtonCallbackData.ACCOUNTING_CALLBACK_DATA)

        self.econometrics_topic_btn = InlineKeyboardButton(self.button_headings.ECONOMETRICS_HEADING,
                                                    callback_data=ButtonCallbackData.ECONOMETRICS_CALLBACK_DATA)

        self.other_economy_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_ECONOMY_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_ECONOMY_CALLBACK_DATA)

        
        self.economy_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.economy_menu_keyboard.add(self.logistics_topic_btn, self.macroeconomics_topic_btn,
                                    self.marketing_topic_btn, self.management_topic_btn, 
                                    self.microeconomics_topic_btn, self.taxarion_topic_btn,
                                    self.personnel_management_topic_btn, self.economy_topic_btn,
                                    self.accounting_topic_btn, self.econometrics_topic_btn,
                                    self.other_economy_topic_btn)