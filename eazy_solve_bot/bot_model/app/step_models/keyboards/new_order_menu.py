from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData
from bot_model.app.db.requests.main_requests import main_request
from bot_model.app.db.requests.order_request import order_request
from bot_model.app.db.requests.telegram_requests import telegram_request
from bot_model.app.db.requests.user_requests import user_request
from settings.general.order_state import ORDER_STATE, OrderStateEnum, STATE_ORDER


class NewOrderMenuKeyboard:
    def __init__(self, language: str, user_id: int) -> None:
        self.button_headings = ButtonHeadings(language)

        self.new_order_by_admin_btn = InlineKeyboardButton(self.button_headings.NEW_ORDER_BY_ADMIN_HEADING,
                                                    callback_data=ButtonCallbackData.NEW_ORDER_BY_ADMIN_CALLBACK_DATA)
        
        self.new_order_by_bot_btn = InlineKeyboardButton(self.button_headings.NEW_ORDER_BY_BOT_HEADING,
                                                    callback_data=ButtonCallbackData.NEW_ORDER_BY_BOT_CALLBACK_DATA)

        self.unfinished_order_btn = InlineKeyboardButton(self.button_headings.UNFINISHED_ORDER_HEADING,
                                                    callback_data=ButtonCallbackData.UNFINISHED_ORDER_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)
        
        def check_unfinished_compile_order(tg_id) -> bool:
            order_status_id = main_request.get_order_status_id_with_order_status_name(STATE_ORDER[OrderStateEnum.ORDER_FROZEN])
            user_telegram = telegram_request.get_telegram_id(tg_id)
            user_id = user_request.get_user_id(user_telegram)
            if order_request.get_or_none_status_order_id_with_user_id(user_id, order_status_id) is None:
                return True
            return False
        
        self.new_order_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.new_order_menu_keyboard.add(self.new_order_by_admin_btn)
        self.new_order_menu_keyboard.add(self.new_order_by_bot_btn)

        if not check_unfinished_compile_order(user_id):
            self.new_order_menu_keyboard.add(self.unfinished_order_btn)
        
        self.new_order_menu_keyboard.add(self.back_btn)