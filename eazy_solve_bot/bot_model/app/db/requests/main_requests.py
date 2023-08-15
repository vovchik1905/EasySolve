from typing import Any
from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, Order, OrderChange, Chat, Order_User, TimeZone, db

from bot_model.app.db.requests.telegram_requests import TelegramRequests, telegram_request
from bot_model.app.db.requests.user_requests import UserRequests, user_request
from bot_model.app.db.requests.language_requests import LanguageRequests, language_request
from bot_model.app.db.requests.order_request import OrderRequests, order_request

class MainRequests:
    def __init__(self, db) -> None:
        self.db = db
    
    def get_language_with_tg_id(self, tg_id: int) -> str:
        with self.db:
            telegram_id = telegram_request.get_telegram_id(tg_id)
            user_id = user_request.get_user_id(telegram_id)
            language_id = user_request.get_user_language(user_id)
            language_name = language_request.get_language_name(language_id)
        return language_name
            
    
    def get_privileges_with_tg_id(self, tg_id: int) -> int:
        if telegram_request.get_or_none_telegram_id(tg_id) is None:
            return None
        user_telegram = telegram_request.get_telegram_id(tg_id)
        user_id = user_request.get_user_id(user_telegram)
        user_privileges = user_request.get_user_privileges(user_id)
        return user_privileges
    

    def get_user_balance_with_tg_id(self, tg_id: int) -> int:
        if telegram_request.get_or_none_telegram_id(tg_id) is None:
            return None
        user_telegram = telegram_request.get_telegram_id(tg_id)
        user_id = user_request.get_user_id(user_telegram)
        user_balance = user_request.get_user_balance(user_id)
        return user_balance
    
    def get_time_zone_id(self, time_zone_name: str) -> int:
        with self.db:
            time_zone_id = TimeZone.select(TimeZone.id).where(TimeZone.name == time_zone_name).get().id
        return time_zone_id
    
    #def get_or_none_order_status_with_tg_id(self, tg_id: int) -> Any:
    #    user_telegram = telegram_request.get_telegram_id(tg_id)
    #    user_id = user_request.get_user_id(user_telegram)
    #    order_id = order_request.get_or_none_status_order_id_with_user_id(user_id)
    #    if order_id is None:
    #        return None
    #    order_status = order_request.get_order_status(order_id)
    #    order_status_name = OrderState.select(OrderState.name).where(OrderState.id == order_status).get().name
    #    return order_status_name

    def get_order_status_id_with_order_status_name(self, order_status_name: str) -> int:
        with self.db:
            order_status_id = OrderState.select(OrderState.id).where(OrderState.name == order_status_name).get().id
        return order_status_id
    



main_request = MainRequests(db)