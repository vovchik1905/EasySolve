from typing import Any
from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, OrderSubject, OrderTopic, Order, OrderChange, Chat, Order_User, db


class SourceRequests:
    """"""
    def __init__(self, db) -> None:
        self.db = db
    
    def create_source(self) -> None:
        pass

    def delete_source(self) -> None:
        pass