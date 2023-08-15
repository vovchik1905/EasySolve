from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class SupportMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.become_a_partner_btn = InlineKeyboardButton(self.button_headings.BECOME_A_PARTNER_HEADING,
                                                    callback_data=ButtonCallbackData.BECOME_A_PARTNER_CALLBACK_DATA)
        
        self.become_a_solver_btn = InlineKeyboardButton(self.button_headings.BECOME_A_SOLVER_HEADING,
                                                    callback_data=ButtonCallbackData.BECOME_A_SOLVER_CALLBACK_DATA)

        self.ask_a_question_btn = InlineKeyboardButton(self.button_headings.ASK_A_QUESTION_HEADING,
                                                    callback_data=ButtonCallbackData.ASK_A_QUESTION_CALLBACK_DATA)

        self.faq_btn = InlineKeyboardButton(self.button_headings.FAQ_HEADING,
                                                    callback_data=ButtonCallbackData.FAQ_CALLBACK_DATA)
        
        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                    callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        self.support_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.support_menu_keyboard.add(self.become_a_partner_btn)
        self.support_menu_keyboard.add(self.become_a_solver_btn)
        self.support_menu_keyboard.add(self.ask_a_question_btn)
        self.support_menu_keyboard.add(self.faq_btn)
        self.support_menu_keyboard.add(self.back_btn)