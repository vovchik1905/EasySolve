from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, Order, OrderChange, Chat, Order_User, db


class PaymentInfoRequests:
    def __init__(self, db) -> None:
        self.db = db

    def get_paiment_info_id(self, paiment_info_card_number: str) -> int:
        with self.db:
            payment_info_id = Payment_info.select(Payment_info.id).where(Payment_info.card_number == paiment_info_card_number).get().id
        return payment_info_id


payment_info_request = PaymentInfoRequests(db)