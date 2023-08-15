from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class GetOrderFilesMenuKeyboard:
    def __init__(self, language: str, order_id: int) -> None:
        self.button_headings = ButtonHeadings(language)
        
        self.confirm_files_btn = InlineKeyboardButton(self.button_headings.CONFIRM_FILES_HEADING,
                                                            callback_data=ButtonCallbackData.CONFIRM_FILES_CALLBACK_DATA)

        self.delete_all_files_btn = InlineKeyboardButton(self.button_headings.DELETE_ALL_FILES_HEADING,
                                                                    callback_data=ButtonCallbackData.DELETE_ALL_FILES_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)

        self.get_order_files_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.get_order_files_menu_keyboard.add(self.confirm_files_btn,
                                                        self.delete_all_files_btn,
                                                        self.back_btn)