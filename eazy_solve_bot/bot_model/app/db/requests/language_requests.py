from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, Order, OrderChange, Chat, Order_User, db


class LanguageRequests:
    def __init__(self, db) -> None:
        self.db = db
    
    def get_language_name(self, language_id: int):
        with self.db:
            language_name = Language.select(Language.name).where(Language.id==language_id).get().name
        return language_name
    
    def get_or_none_language_id(self, language_name: str):
        with self.db:
            language_id = Language.get_or_none(name=language_name)
        return language_id
    
    def get_language_id(self, language_name: str):
        with self.db:
            language_id = Language.select(Language.id).where(Language.name==language_name).get().id
        return language_id

language_request = LanguageRequests(db)