from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class BiologyTopicMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.anatomy_topic_btn = InlineKeyboardButton(self.button_headings.ANATOMY_HEADING,
                                                    callback_data=ButtonCallbackData.ANATOMY_CALLBACK_DATA)
        
        self.parasitology_topic_btn = InlineKeyboardButton(self.button_headings.PARASITOLOGY_HEADING,
                                                    callback_data=ButtonCallbackData.PARASITOLOGY_CALLBACK_DATA)

        self.bioinformatics_topic_btn = InlineKeyboardButton(self.button_headings.BIOINFORMATICS_HEADING,
                                                    callback_data=ButtonCallbackData.BIOINFORMATICS_CALLBACK_DATA)

        self.microbiology_topic_btn = InlineKeyboardButton(self.button_headings.MICROBIOLOGY_HEADING,
                                                    callback_data=ButtonCallbackData.MICROBIOLOGY_CALLBACK_DATA)

        self.botany_topic_btn = InlineKeyboardButton(self.button_headings.BOTANY_HEADING,
                                                    callback_data=ButtonCallbackData.BOTANY_CALLBACK_DATA)
        
        self.molecular_biology_topic_btn = InlineKeyboardButton(self.button_headings.MOLECULAR_BIOLOGY_HEADING,
                                                    callback_data=ButtonCallbackData.MOLECULAR_BIOLOGY_CALLBACK_DATA)

        self.zoology_topic_btn = InlineKeyboardButton(self.button_headings.ZOOLOGY_HEADING,
                                                    callback_data=ButtonCallbackData.ZOOLOGY_CALLBACK_DATA)

        self.genetics_topic_btn = InlineKeyboardButton(self.button_headings.GENETICS_HEADING,
                                                    callback_data=ButtonCallbackData.GENETICS_CALLBACK_DATA)

        self.virology_topic_btn = InlineKeyboardButton(self.button_headings.VIROLOGY_HEADING,
                                                    callback_data=ButtonCallbackData.VIROLOGY_CALLBACK_DATA)

        self.other_biology_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_BIOLOGY_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_BIOLOGY_CALLBACK_DATA)

        
        self.biology_topic_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.biology_topic_menu_keyboard.add(self.anatomy_topic_btn, self.parasitology_topic_btn,
                                                self.bioinformatics_topic_btn, self.microbiology_topic_btn, 
                                                self.botany_topic_btn, self.molecular_biology_topic_btn,
                                                self.zoology_topic_btn, self.genetics_topic_btn,
                                                self.virology_topic_btn, self.other_biology_topic_btn)