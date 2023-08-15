from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData

class CheckingUserSubscriptionMenu:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        self.check_btn = InlineKeyboardButton(self.button_headings.USER_SUBSCRIPTION_CHECK_HEADING,
                                                    callback_data=ButtonCallbackData.USER_SUBSCRIPTION_CHECK_CALLBACK_DATA)
        
        self.checking_user_subscription_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.checking_user_subscription_menu_keyboard.add(self.check_btn)