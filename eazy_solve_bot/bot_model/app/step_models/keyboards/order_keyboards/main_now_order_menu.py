from typing import Any
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData
from bot_model.app.db.requests.order_request import order_request
from bot_model.app.db.requests.user_requests import user_request
from bot_model.app.db.requests.telegram_requests import telegram_request
from bot_model.app.db.requests.file_requests import file_request

from settings.general.order_subject import ORDER_SUBJECT, OrderSubject


class MainNowOrderMenuKeyboard:
    def __init__(self, language: str, order_id: int) -> None:
        
        def check_subject_complete(order_id: int) -> Any:
            order_subject = order_request.get_order_subject_name(order_id)
            if order_subject is None or ORDER_SUBJECT[order_subject] is OrderSubject.NONE_SBJ:
                return None
            else:
                return order_subject

        def check_comment_complete(order_id: int) -> Any:
            order_comment = order_request.get_order_comment(order_id)
            return order_comment
        
        def check_files_complete(order_id: int) -> Any:
            order_files = file_request.get_all_order_files(order_id)
            return order_files
        
        def check_deadline_time_complete(order_id: int) -> Any:
            order_deadline_time = order_request.get_order_duration_time(order_id)
            return order_deadline_time
        
        def check_number_of_tasks(order_id: int) -> Any:
            order_number_of_tasks = order_request.get_order_number_of_tasks(order_id)
            return order_number_of_tasks

        NONE_VALUE = "❓"
        DONE_VALUE = "✅"

        self.button_headings = ButtonHeadings(language)

        self.new_standart_order_importance_btn = InlineKeyboardButton(self.button_headings.NEW_NOW_ORDER_IMPORTANCE_HEADING,
                                                    callback_data=ButtonCallbackData.NEW_NOW_ORDER_IMPORTANCE_CALLBACK_DATA)

        #order_subject_value = check_subject_complete(order_id)
        if check_subject_complete(order_id) is None:
            subject_btn_heading = f"{self.button_headings.NEW_STANDART_ORDER_SUBJECT_HEADING}: {NONE_VALUE}"
        else:
            subject_btn_heading = f"{check_subject_complete(order_id)}: {DONE_VALUE}"
        
        self.new_standart_order_subject_btn = InlineKeyboardButton(subject_btn_heading,
                                                    callback_data=ButtonCallbackData.NEW_STANDART_ORDER_SUBJECT_CALLBACK_DATA)
        

        if check_comment_complete(order_id) is None:
            comment_btn_heading = f"{self.button_headings.NEW_STANDART_ORDER_COMMENT_HEADING}: {NONE_VALUE}"
        else:
            comment_btn_heading = f"{self.button_headings.NEW_STANDART_ORDER_COMMENT_HEADING}: {DONE_VALUE}"

        self.new_standart_order_comment_btn = InlineKeyboardButton(comment_btn_heading,
                                                    callback_data=ButtonCallbackData.NEW_STANDART_ORDER_COMMENT_CALLBACK_DATA)


        if check_files_complete(order_id) is None:
            files_btn_heading = f"{self.button_headings.NEW_STANDART_ORDER_FILES_HEADING}: {NONE_VALUE}"
        else:
            files_btn_heading = f"{self.button_headings.NEW_STANDART_ORDER_FILES_HEADING}: {DONE_VALUE}"

        self.new_standart_order_files_btn = InlineKeyboardButton(files_btn_heading,
                                                callback_data=ButtonCallbackData.NEW_STANDART_ORDER_FILES_CALLBACK_DATA)


        if check_deadline_time_complete(order_id) is None:
            deadline_time_btn_heading = f"{self.button_headings.NEW_STANDART_ORDER_DEADLINE_TIME_HEADING}: {NONE_VALUE}"
        else:
            deadline_time_btn_heading = f"{self.button_headings.NEW_STANDART_ORDER_DEADLINE_TIME_HEADING}: {DONE_VALUE}"

        self.new_standart_order_deadline_time_btn = InlineKeyboardButton(deadline_time_btn_heading,
                                                    callback_data=ButtonCallbackData.NEW_STANDART_ORDER_DEADLINE_TIME_CALLBACK_DATA)

        if check_number_of_tasks(order_id) is None:
            number_of_tasks_btn_heading = f"{self.button_headings.NEW_NOW_ORDER_NUMBER_OF_TASKS_HEADING}: {NONE_VALUE}"
        else:
            number_of_tasks_btn_heading = f"{self.button_headings.NEW_NOW_ORDER_NUMBER_OF_TASKS_HEADING}: {DONE_VALUE}"
        
        self.number_of_tasks_btn = InlineKeyboardButton(number_of_tasks_btn_heading,
                                                        callback_data=ButtonCallbackData.NEW_NOW_ORDER_NUMBER_OF_TASKS_CALLBACK_DATA)

        self.up_order_settings_btn = InlineKeyboardButton(self.button_headings.UP_ORDER_SETTINGS_HEADING,
                                                            callback_data=ButtonCallbackData.UP_ORDER_SETTINGS_CALLBACK_DATA)

        self.send_order_to_solvers_btn = InlineKeyboardButton(self.button_headings.SEND_ORDER_TO_SOLVERS_HEADING,
                                                            callback_data=ButtonCallbackData.SEND_ORDER_TO_SOLVERS_CALLBACK_DATA)


        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        
        self.main_now_order_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.main_now_order_menu_keyboard.add(self.new_standart_order_importance_btn,
                                                self.new_standart_order_subject_btn,
                                                self.new_standart_order_comment_btn,
                                                self.new_standart_order_files_btn,
                                                self.new_standart_order_deadline_time_btn,
                                                self.number_of_tasks_btn)
                                                
        self.main_now_order_menu_keyboard.add(self.up_order_settings_btn)
        self.main_now_order_menu_keyboard.add(self.send_order_to_solvers_btn)
        self.main_now_order_menu_keyboard.add(self.back_btn)