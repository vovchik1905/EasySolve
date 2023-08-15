from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData
from bot_model.app.db.requests.main_requests import main_request


class ClientAndSolverMainMenuKeyboard:
    def __init__(self, language: str, user_id: int) -> None:
        self.button_headings = ButtonHeadings(language)

        self.new_order_btn = InlineKeyboardButton(self.button_headings.NEW_ORDER_HEADING,
                                                    callback_data=ButtonCallbackData.NEW_ORDER_CALLBACK_DATA)
        
        self.active_orders_btn = InlineKeyboardButton(self.button_headings.ACTIVE_ORDERS_HEADING,
                                                        callback_data=ButtonCallbackData.ACTIVE_ORDERS_CALLBACK_DATA)
        
        self.my_profile_btn = InlineKeyboardButton(self.button_headings.MY_PROFILE_HEADING,
                                                    callback_data=ButtonCallbackData.MY_PROFILE_CALLBACK_DATA)
        
        self.balance_btn = InlineKeyboardButton(self.button_headings.BALANCE_HEADING + f" {main_request.get_user_balance_with_tg_id(user_id)}",
                                                callback_data=ButtonCallbackData.BALANCE_CALLBACK_DATA)
        
        self.support_btn = InlineKeyboardButton(self.button_headings.SUPPORT_HEADING,
                                                callback_data=ButtonCallbackData.SUPPORT_CALLBACK_DATA)
        
        self.reviews_btn = InlineKeyboardButton(self.button_headings.REVIEWS_HEADING,
                                                callback_data=ButtonCallbackData.REVIEWS_CALLBACK_DATA)
        
        self.affiliate_program_btn = InlineKeyboardButton(self.button_headings.AFFILIATE_PROGRAM_HEADING,
                                                            callback_data=ButtonCallbackData.AFFILIATE_PROGRAM_CALLBACK_DATA)
        
        self.solver_menu_btn = InlineKeyboardButton(self.button_headings.SOLVER_MENU_HEADING,
                                                    callback_data=ButtonCallbackData.SOLVER_MENU_CALLBACK_DATA)
        
        self.client_and_solver_main_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.client_and_solver_main_menu_keyboard.add(self.new_order_btn)
        self.client_and_solver_main_menu_keyboard.add(self.active_orders_btn)
        self.client_and_solver_main_menu_keyboard.add(self.my_profile_btn)
        self.client_and_solver_main_menu_keyboard.add(self.balance_btn)
        self.client_and_solver_main_menu_keyboard.add(self.support_btn, self.reviews_btn)
        self.client_and_solver_main_menu_keyboard.add(self.affiliate_program_btn)
        self.client_and_solver_main_menu_keyboard.add(self.solver_menu_btn)