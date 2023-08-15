from typing import Any
from bot_model.app.db.requests.telegram_requests import TelegramRequests
from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, Order, OrderChange, Chat, Order_User, TimeZone, db
from bot_model.app.db.runtime_storage.runtime_storage import *
from settings.general.general_settings import GeneralSettings


class UserRequests:
    def __init__(self, db) -> None:
        self.db = db
    
    def create_new_user(self, user_telegram: int, user_language: int, user_currency: int,
                       user_payment_info: int, user_privileges: int = 1, user_client_status: int = 4,
                       user_solver: bool = False, user_solver_status: int = 4):
        """"""
        with self.db:
            RuntimeStorageUser.time_zone = TimeZone.select(
                TimeZone.id).where(TimeZone.name == GeneralSettings.BOT_TIME_ZONE).get().id
            create_user = User(telegram=user_telegram,
                                privileges=user_privileges,
                                language=user_language,
                                time_zone=RuntimeStorageUser.time_zone,
                                currency=user_currency,
                                payment_info=user_payment_info,
                                client_status=user_client_status,
                                balance=0,
                                refund_balance=0,
                                client_orders_num=0,
                                client_disputs_percent=0,
                                client_total_sum=0,
                                solver=user_solver,
                                solver_status=user_solver_status,
                                solver_orders_num=0,
                                solver_disputs_percent=0,
                                solver_total_sum=0)
            create_user.save()
    
    def get_or_none_user_id(self, user_telegram: int) -> int:
        with self.db:
            user_id = User.get_or_none(telegram=user_telegram)
        return user_id
    
    def get_user_id(self, user_telegram: int) -> int:
        """"""
        if self.get_or_none_user_id(user_telegram) is None:
            return None
        with self.db:
            user_id = User.select(User.id).where(User.telegram==user_telegram).get().id
        return user_id
    
    def update_user_privileges(self, user_id: int, user_privileges: int) -> None:
        with self.db:
            update_user_privileges = User.get(User.id==user_id)
            update_user_privileges.privileges = user_privileges
            update_user_privileges.save()
    
    def update_user_language(self, user_id: int, user_language: int) -> None:
        with self.db:
            update_user_language = User.get(User.id==user_id)
            update_user_language.language = user_language
            update_user_language.save()
    
    def update_user_time_zone(self, user_id: int, user_time_zone: int) -> None:
        with self.db:
            update_user_time_zone = User.get(User.id==user_id)
            update_user_time_zone.time_zone = user_time_zone
            update_user_time_zone.save()
    
    def update_user_currency(self, user_id: int, user_currency: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.currency = user_currency
            update_user_currency.save()
    
    def update_user_payment_info(self, user_id: int, user_payment_info: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.payment_info = user_payment_info
            update_user_currency.save()
    
    def update_user_client_status(self, user_id: int, user_client_status: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.client_status = user_client_status
            update_user_currency.save()
    
    def update_user_balance(self, user_id: int, user_balance: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.balance = user_balance
            update_user_currency.save()

    def update_user_refund_balance(self, user_id: int, user_refund_balance: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.refund_balance = user_refund_balance
            update_user_currency.save()
    
    def update_user_client_orders_num(self, user_id: int, user_client_orders_num: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.client_orders_num = user_client_orders_num
            update_user_currency.save()
    
    def update_user_client_disputs_percent(self, user_id: int, user_client_disputs_percent: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.client_disputs_percent = user_client_disputs_percent
            update_user_currency.save()
    
    def update_user_client_total_sum(self, user_id: int, user_client_total_sum: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.client_total_sum = user_client_total_sum
            update_user_currency.save()
    
    def update_user_solver(self, user_id: int, user_solver: bool) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.solver = user_solver
            update_user_currency.save()
    
    def update_user_solver_status(self, user_id: int, user_solver_status: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.solver_status = user_solver_status
            update_user_currency.save()
    
    def update_user_solver_orders_num(self, user_id: int, user_solver_orders_num: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.solver_orders_num = user_solver_orders_num
            update_user_currency.save()
    
    def update_user_solver_disputs_percent(self, user_id: int, user_solver_disputs_percent: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.solver_disputs_percent = user_solver_disputs_percent
            update_user_currency.save()
    
    def update_user_solver_total_sum(self, user_id: int, user_solver_total_sum: int) -> None:
        with self.db:
            update_user_currency = User.get(User.id==user_id)
            update_user_currency.solver_total_sum = user_solver_total_sum
            update_user_currency.save()
    
    def get_user_privileges(self, user_id: int) -> int:
        with self.db:
            user_privileges = User.select(User.privileges).where(User.id == user_id).get().privileges
        return user_privileges
    
    def get_user_language(self, user_id: int) -> int:
        with self.db:
            user_language = User.select(User.language).where(User.id == user_id).get().language
        return user_language
    
    def get_user_balance(self, user_id: int) -> int:
        with self.db:
            user_balance = User.select(User.balance).where(User.id == user_id).get().balance
        return user_balance
user_request = UserRequests(db)