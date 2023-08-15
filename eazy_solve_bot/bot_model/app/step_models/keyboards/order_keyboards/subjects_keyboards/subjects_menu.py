from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class SubjectMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.maths_subject_btn = InlineKeyboardButton(self.button_headings.MATHS_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.MATHS_SUBJECT_CALLBACK_DATA)
        
        self.physics_subject_btn = InlineKeyboardButton(self.button_headings.PHYSICS_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.PHYSICS_SUBJECT_CALLBACK_DATA)

        self.it_subject_btn = InlineKeyboardButton(self.button_headings.IT_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.IT_SUBJECT_CALLBACK_DATA)

        self.engineering_subject_btn = InlineKeyboardButton(self.button_headings.ENGINEERING_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.ENGINEERING_SUBJECT_CALLBACK_DATA)

        self.economy_subject_btn = InlineKeyboardButton(self.button_headings.ECONOMY_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.ECONOMY_SUBJECT_CALLBACK_DATA)
        
        self.chemistry_subject_btn = InlineKeyboardButton(self.button_headings.CHEMISTRY_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.CHEMISTRY_SUBJECT_CALLBACK_DATA)

        self.languages_subject_btn = InlineKeyboardButton(self.button_headings.LANGUAGES_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.LANGUAGES_SUBJECT_CALLBACK_DATA)

        self.biology_subject_btn = InlineKeyboardButton(self.button_headings.BIOLOGY_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.BIOLOGY_SUBJECT_CALLBACK_DATA)

        self.geography_subject_btn = InlineKeyboardButton(self.button_headings.GEOGRAPHY_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.GEOGRAPHY_SUBJECT_CALLBACK_DATA)

        self.humanitarian_subject_btn = InlineKeyboardButton(self.button_headings.HUMANITARIAN_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.HUMANITARIAN_SUBJECT_CALLBACK_DATA)

        self.registration_subject_btn = InlineKeyboardButton(self.button_headings.REGISTRATION_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.REGISTRATION_SUBJECT_CALLBACK_DATA)

        self.other_subject_btn = InlineKeyboardButton(self.button_headings.OTHER_SUBJECT_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_SUBJECT_CALLBACK_DATA)
        
        self.subject_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.subject_menu_keyboard.add(self.maths_subject_btn, self.physics_subject_btn,
                                    self.it_subject_btn, self.engineering_subject_btn,
                                    self.economy_subject_btn, self.chemistry_subject_btn,
                                    self.languages_subject_btn, self.biology_subject_btn,
                                    self.geography_subject_btn, self.humanitarian_subject_btn,
                                    self.registration_subject_btn, self.other_subject_btn)
        