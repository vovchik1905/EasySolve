from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, Order, OrderChange, Chat, Order_User, db


class CurrencyRequests:
    def __init__(self, db) -> None:
        self.db = db

    def get_currency_id(self, currency_name: str) -> int:
        with self.db:
            currency_id = Currency.select(Currency.id).where(Currency.name == currency_name).get().id
        return currency_id


currency_request = CurrencyRequests(db)