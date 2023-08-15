from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData, ButtonURLData


class AffiliateProgramMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)
        
        self.list_affiliate_links_btn = InlineKeyboardButton(self.button_headings.LIST_AFFILIATE_LINKS_HEADING,
                                                    callback_data=ButtonCallbackData.LIST_AFFILIATE_LINKS_CALLBACK_DATA)

        self.create_affiliate_link_btn = InlineKeyboardButton(self.button_headings.CREATE_AFFILIATE_LINK_HEADING,
                                                    callback_data=ButtonCallbackData.CREATE_AFFILIATE_LINK_CALLBACK_DATA)
        
        self.affiliate_program_statistics_btn = InlineKeyboardButton(self.button_headings.AFFILIATE_PROGRAM_STATISTICS_HEADING,
                                                callback_data=ButtonCallbackData.AFFILIATE_PROGRAM_STATISTICS_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                    callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        self.affiliate_program_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.affiliate_program_menu_keyboard.add(self.affiliate_program_statistics_btn)
        self.affiliate_program_menu_keyboard.add(self.list_affiliate_links_btn, self.create_affiliate_link_btn)
        self.affiliate_program_menu_keyboard.add(self.back_btn)