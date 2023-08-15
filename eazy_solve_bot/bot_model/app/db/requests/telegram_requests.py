from typing import Any
from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, Order, OrderChange, Chat, Order_User, db


class TelegramRequests:
    def __init__(self, db) -> None:
        self.db = db

    def create_new_telegram(self, telegram_tg_id: int, telegram_tg_name: str = None,
                            telegram_tg_sername: str = None, telegram_tg_username: str = None) -> None:
        with self.db:
            create_tg = Telegram(tg_id=telegram_tg_id,
                                tg_name=telegram_tg_name,
                                tg_sername=telegram_tg_sername,
                                tg_username=telegram_tg_username)
            create_tg.save()
    
    def get_or_none_telegram_id(self, telegram_tg_id: int) -> int:
        with self.db:
            telegram_id = Telegram.get_or_none(tg_id=telegram_tg_id)
        return telegram_id
    
    def get_telegram_id(self, telegram_tg_id: int) -> int:
        if self.get_or_none_telegram_id(telegram_tg_id) is None:
            return None
        with self.db:
            telegram_id = Telegram.select(Telegram.id).where(Telegram.tg_id == telegram_tg_id).get().id
        return telegram_id
    
    def get_telegram_tg_name(self, telegram_tg_id: int) -> str:
        with self.db:
            telegram_tg_name = Telegram.select(Telegram.tg_name).where(Telegram.tg_id == telegram_tg_id).get().tg_name
        return telegram_tg_name
    
    def get_telegram_tg_sername(self, telegram_tg_id: int) -> str:
        with self.db:
            telegram_tg_sername = Telegram.select(Telegram.tg_sername).where(Telegram.tg_id == telegram_tg_id).get().tg_sername
        return telegram_tg_sername
    
    def get_telegram_tg_username(self, telegram_tg_id: int) -> str:
        with self.db:
            telegram_tg_username = Telegram.select(Telegram.tg_username).where(Telegram.tg_id == telegram_tg_id).get().tg_username
        return telegram_tg_username

telegram_request = TelegramRequests(db)