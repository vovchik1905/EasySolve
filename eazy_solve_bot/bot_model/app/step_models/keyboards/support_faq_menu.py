from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData, ButtonURLData


class SupportFaqMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.faq_for_clients_btn = InlineKeyboardButton(text=self.button_headings.FAQ_FOR_CLIENTS_HEADING,
                                                        url=ButtonURLData.FAQ_FOR_CLIENTS_URL_DATA)
        
        self.faq_for_solvers_btn = InlineKeyboardButton(text=self.button_headings.FAQ_FOR_SOLVERS_HEADING,
                                                        url=ButtonURLData.FAQ_FOR_SOLVERS_URL_DATA)

        self.faq_for_partners_btn = InlineKeyboardButton(text=self.button_headings.FAQ_FOR_PARTNERS_HEADING,
                                                        url=ButtonURLData.FAQ_FOR_PARTNERS_URL_DATA)
        
        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                    callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        self.support_faq_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.support_faq_menu_keyboard.add(self.faq_for_clients_btn)
        self.support_faq_menu_keyboard.add(self.faq_for_solvers_btn)
        self.support_faq_menu_keyboard.add(self.faq_for_partners_btn)
        self.support_faq_menu_keyboard.add(self.back_btn)