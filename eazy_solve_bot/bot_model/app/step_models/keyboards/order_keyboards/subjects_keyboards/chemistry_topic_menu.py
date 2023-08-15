from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class ChemistryMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.organic_chemistry_topic_btn = InlineKeyboardButton(self.button_headings.ORGANIC_CHEMISTRY_HEADING,
                                                    callback_data=ButtonCallbackData.ORGANIC_CHEMISTRY_CALLBACK_DATA)
        
        self.analytical_chemistry_topic_btn = InlineKeyboardButton(self.button_headings.ANALYTICAL_CHEMISTRY_HEADING,
                                                    callback_data=ButtonCallbackData.ANALYTICAL_CHEMISTRY_CALLBACK_DATA)

        self.general_chemistry_topic_btn = InlineKeyboardButton(self.button_headings.GENERAL_CHEMISTRY_HEADING,
                                                    callback_data=ButtonCallbackData.GENERAL_CHEMISTRY_CALLBACK_DATA)

        self.biochemistry_topic_btn = InlineKeyboardButton(self.button_headings.BIOCHEMISTRY_HEADING,
                                                    callback_data=ButtonCallbackData.BIOCHEMISTRY_CALLBACK_DATA)

        self.physical_chemistry_topic_btn = InlineKeyboardButton(self.button_headings.PHYSICAL_CHEMISTRY_HEADING,
                                                    callback_data=ButtonCallbackData.PHYSICAL_CHEMISTRY_CALLBACK_DATA)
        
        self.inorganic_chemistry_topic_btn = InlineKeyboardButton(self.button_headings.INORGANIC_CHEMISTRY_HEADING,
                                                    callback_data=ButtonCallbackData.INORGANIC_CHEMISTRY_CALLBACK_DATA)

        self.other_chemistry_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_CHEMISTRY_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_CHEMISTRY_CALLBACK_DATA)

        
        self.chemistry_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.chemistry_menu_keyboard.add(self.organic_chemistry_topic_btn, self.analytical_chemistry_topic_btn,
                                    self.general_chemistry_topic_btn, self.biochemistry_topic_btn, 
                                    self.physical_chemistry_topic_btn, self.inorganic_chemistry_topic_btn,
                                    self.other_chemistry_topic_btn)