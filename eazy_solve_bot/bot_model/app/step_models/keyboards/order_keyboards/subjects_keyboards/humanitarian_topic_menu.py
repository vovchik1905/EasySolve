from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class HumanitarianTopicMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.history_topic_btn = InlineKeyboardButton(self.button_headings.HISTORY_HEADING,
                                                    callback_data=ButtonCallbackData.HISTORY_CALLBACK_DATA)
        
        self.design_topic_btn = InlineKeyboardButton(self.button_headings.DESIGN_HEADING,
                                                    callback_data=ButtonCallbackData.DESIGN_CALLBACK_DATA)

        self.obzh_topic_btn = InlineKeyboardButton(self.button_headings.OBZH_HEADING,
                                                    callback_data=ButtonCallbackData.OBZH_CALLBACK_DATA)

        self.philosophy_topic_btn = InlineKeyboardButton(self.button_headings.PHILOSOPHY_HEADING,
                                                    callback_data=ButtonCallbackData.PHILOSOPHY_CALLBACK_DATA)

        self.law_topic_btn = InlineKeyboardButton(self.button_headings.LAW_HEADING,
                                                    callback_data=ButtonCallbackData.LAW_CALLBACK_DATA)
        
        self.other_humanitarian_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_HUMANITARIAN_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_HUMANITARIAN_CALLBACK_DATA)

        
        self.humanitarian_topic_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.humanitarian_topic_menu_keyboard.add(self.history_topic_btn, self.design_topic_btn,
                                                self.obzh_topic_btn, self.philosophy_topic_btn, 
                                                self.law_topic_btn, self.other_humanitarian_topic_btn)