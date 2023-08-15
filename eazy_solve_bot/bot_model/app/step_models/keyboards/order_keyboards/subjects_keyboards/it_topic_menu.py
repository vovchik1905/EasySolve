from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class ITMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.basic_it_topic_btn = InlineKeyboardButton(self.button_headings.BASIC_IT_HEADING,
                                                    callback_data=ButtonCallbackData.BASIC_IT_CALLBACK_DATA)   #
        
        self.c_it_topic_btn = InlineKeyboardButton(self.button_headings.C_IT_HEADING,
                                                    callback_data=ButtonCallbackData.C_IT_CALLBACK_DATA)   #

        self.c_sharp_it_topic_btn = InlineKeyboardButton(self.button_headings.C_SHARP_IT_HEADING,
                                                    callback_data=ButtonCallbackData.C_SHARP_IT_CALLBACK_DATA)   #

        self.c_plus_plus_it_topic_btn = InlineKeyboardButton(self.button_headings.C_PLUS_PLUS_IT_HEADING,
                                                    callback_data=ButtonCallbackData.C_PLUS_PLUS_IT_CALLBACK_DATA)   #
        
        self.delphi_topic_btn = InlineKeyboardButton(self.button_headings.DELPHI_IT_HEADING,
                                                    callback_data=ButtonCallbackData.DELPHI_IT_CALLBACK_DATA)   #

        self.exel_it_topic_btn = InlineKeyboardButton(self.button_headings.EXCEL_IT_HEADING,
                                                    callback_data=ButtonCallbackData.EXCEL_IT_CALLBACK_DATA)   #

        self.java_it_topic_btn = InlineKeyboardButton(self.button_headings.JAVA_IT_HEADING,
                                                    callback_data=ButtonCallbackData.JAVA_IT_CALLBACK_DATA)   #

        self.java_script_topic_btn = InlineKeyboardButton(self.button_headings.JAVA_SCRIPT_HEADING,
                                                    callback_data=ButtonCallbackData.JAVA_SCRIPT_CALLBACK_DATA)   #

        self.go_it_topic_btn = InlineKeyboardButton(self.button_headings.GO_IT_HEADING,
                                                    callback_data=ButtonCallbackData.GO_IT_CALLBACK_DATA)   #

        self.matlab_it_topic_btn = InlineKeyboardButton(self.button_headings.MATLAB_IT_HEADING,
                                                    callback_data=ButtonCallbackData.MATLAB_IT_CALLBACK_DATA)   #
        
        self.python_it_topic_btn = InlineKeyboardButton(self.button_headings.PYTHON_IT_HEADING,
                                                    callback_data=ButtonCallbackData.PYTHON_IT_CALLBACK_DATA)

        self.php_it_topic_btn = InlineKeyboardButton(self.button_headings.PHP_IT_HEADING,
                                                    callback_data=ButtonCallbackData.PHP_IT_CALLBACK_DATA)

        self.data_base_it_topic_btn = InlineKeyboardButton(self.button_headings.DATA_BASE_IT_HEADING,
                                                    callback_data=ButtonCallbackData.DATA_BASE_IT_CALLBACK_DATA)

        self.latex_it_topic_btn = InlineKeyboardButton(self.button_headings.LATEX_IT_HEADING,
                                                    callback_data=ButtonCallbackData.LATEX_IT_CALLBACK_DATA)

        self.lazarus_topic_btn = InlineKeyboardButton(self.button_headings.LAZARUS_HEADING,
                                                    callback_data=ButtonCallbackData.LAZARUS_CALLBACK_DATA)

        self.pascal_it_topic_btn = InlineKeyboardButton(self.button_headings.PASCAL_IT_HEADING,
                                                    callback_data=ButtonCallbackData.PASCAL_IT_CALLBACK_DATA)

        self.r_it_topic_btn = InlineKeyboardButton(self.button_headings.R_IT_HEADING,
                                                    callback_data=ButtonCallbackData.R_IT_CALLBACK_DATA)

        self.other_it_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_IT_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_IT_CALLBACK_DATA)

        
        self.it_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.it_menu_keyboard.add(self.basic_it_topic_btn, self.c_it_topic_btn,
                                    self.c_sharp_it_topic_btn, self.c_plus_plus_it_topic_btn,
                                    self.delphi_topic_btn, self.exel_it_topic_btn,
                                    self.java_it_topic_btn, self.java_script_topic_btn,
                                    self.go_it_topic_btn, self.matlab_it_topic_btn,
                                    self.python_it_topic_btn, self.php_it_topic_btn,
                                    self.data_base_it_topic_btn, self.latex_it_topic_btn,
                                    self.lazarus_topic_btn, self.pascal_it_topic_btn,
                                    self.r_it_topic_btn, self.other_it_topic_btn)