from peewee import *
from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
    Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
    File, OrderSubject, OrderTopic, Order, OrderChange, Chat, Order_User, OrderStateTime, TimeZone, db
from settings.general.general_settings import GeneralSettings
from settings.general.order_state import ORDER_STATE
from settings.general.order_subject import ORDER_SUBJECT
from settings.general.order_topic import ORDER_TOPIC
from bot_model.app.db.runtime_storage.runtime_storage import *


class CreateDataBase:
    def __init__(self, db) -> None:
        self.db = db

    @property
    def create_db(self):
        with self.db:
            self.db.create_tables([ClientStatus, SolverStatus, OrderFormat, OrderState,
                                   OrderImportance, Language, Telegram, Currency, Payment_info,
                                   User, ClientReview, SolverReview, Source, Source_User,
                                   File, OrderSubject, OrderTopic, Order, OrderChange, Chat,
                                   Order_User, OrderStateTime, TimeZone])

    def setting_up_language_table(self):
        data_source = []
        for language in GeneralSettings.LANGUAGES:
            if GeneralSettings.LANGUAGES[language] is True:
                data_source.append(language)

        with self.db:
            for language_name in data_source:
                create_language = Language(name=language_name)
                create_language.save()

    def setting_up_currency_table(self):
        # дописать курс валют
        data_source = []
        for currency in GeneralSettings.CURRENCY:
            if GeneralSettings.CURRENCY[currency] is True:
                data_source.append((currency))
        with self.db:
            for currency_name in data_source:
                create_currency = Currency(name=currency_name)
                create_currency.save()

    def setting_up_client_status_table(self):
        data_source = []
        for client_status in GeneralSettings.CLIENT_STATUS_SETTINGS:
            data_source.append((client_status))
        with self.db:
            for client_status_name in data_source:
                create_client_status = ClientStatus(name=client_status_name)
                create_client_status.save()

    def setting_up_solver_status_table(self):
        data_source = []
        for solver_status in GeneralSettings.SOLVER_STATUS_SETTINGS:
            data_source.append((solver_status))
        with self.db:
            for solver_status_name in data_source:
                create_solver_status = SolverStatus(name=solver_status_name)
                create_solver_status.save()

    def setting_up_order_format_table(self):
        data_source = []
        for order_format in GeneralSettings.ORDER_FORMAT_SETTINGS:
            data_source.append((order_format))
        with self.db:
            for order_format_name in data_source:
                create_order_format = OrderFormat(name=order_format_name)
                create_order_format.save()

    def setting_up_order_importance_table(self):
        data_source = []
        for order_importance in GeneralSettings.ORDER_IMPORTANCE_SETTINGS:
            data_source.append((order_importance))
        with self.db:
            for order_importance_name in data_source:
                create_order_importance = OrderImportance(
                    name=order_importance_name)
                create_order_importance.save()

    def setting_up_order_state_table(self):
        data_source = []
        for order_state in ORDER_STATE:
            data_source.append(order_state)
        with self.db:
            for order_state_name in data_source:
                create_order_state = OrderState(name=order_state_name)
                create_order_state.save()
    
    def setting_up_order_subject_table(self):
        data_source = []
        for order_subject in ORDER_SUBJECT:
            data_source.append(order_subject)
        with self.db:
            for order_subject_name in data_source:
                create_order_subject = OrderSubject(name=order_subject_name)
                create_order_subject.save()

    def setting_up_order_topic_table(self):
        data_source = []
        for order_topic in ORDER_TOPIC:
            data_source.append(order_topic)
        with self.db:
            for order_topic_name in data_source:
                create_order_topic = OrderTopic(name=order_topic_name)
                create_order_topic.save()
    
    def setting_up_payment_info_table(self):
        card_number = GeneralSettings.BASE_PAYMENT_INFO["card_number"]
        card_bank = GeneralSettings.BASE_PAYMENT_INFO["card_bank"]
        card_phone = GeneralSettings.BASE_PAYMENT_INFO["card_phone"]
        cardholler_name = GeneralSettings.BASE_PAYMENT_INFO["cardholler_name"]
        create_base_payment_info = Payment_info(card_number = card_number,
                                                card_bank = card_bank,
                                                card_phone = card_phone,
                                                cardholler_name = cardholler_name)
        create_base_payment_info.save()
    
    def setting_up_time_zone_table(self):
        data_source = []
        for time_zone in GeneralSettings.TIME_ZONES:
            data_source.append((time_zone, GeneralSettings.TIME_ZONES[time_zone]))
        with self.db:
            for time_zone_values in data_source:
                create_time_zone = TimeZone(name=time_zone_values[0],
                                            time_difference=time_zone_values[1])
                create_time_zone.save()
        

    @property
    def setting_up_all_tables(self):
        self.setting_up_language_table()
        self.setting_up_currency_table()
        self.setting_up_client_status_table()
        self.setting_up_solver_status_table()
        self.setting_up_order_format_table()
        self.setting_up_order_importance_table()
        self.setting_up_order_state_table()
        self.setting_up_order_subject_table()
        self.setting_up_order_topic_table()
        self.setting_up_payment_info_table()
        self.setting_up_time_zone_table()

    def create_partner(self, partner_telegram: tuple, partner_language: str, partner_currency: str,
                       partner_payment_info: tuple, partner_privileges: int = 3, partner_client_status: str = "PLATINUM",
                       partner_solver: bool = True, partner_solver_status: str = "PLATINUM"):
        """"""
        partner_tg_id, partner_tg_name, partner_tg_sername, partner_tg_usename = partner_telegram
        partner_card_number, partner_card_bank, partner_card_phone, partner_cardholler_name = partner_payment_info
        with self.db:
            create_partner_telegram = Telegram(tg_id=partner_tg_id,
                                               tg_name=partner_tg_name,
                                               tg_sername=partner_tg_sername,
                                               tg_username=partner_tg_usename)
            create_partner_telegram.save()
            create_partner_payment_info = Payment_info(card_number=partner_card_number,
                                                       card_bank=partner_card_bank,
                                                       card_phone=partner_card_phone,
                                                       cardholler_name=partner_cardholler_name)
            create_partner_payment_info.save()

            RuntimeStorageUser.telegram = Telegram.select(
                Telegram.id).where(Telegram.tg_id == partner_tg_id).get().id

            RuntimeStorageUser.privileges = partner_privileges

            RuntimeStorageUser.language = Language.select(
                Language.id).where(Language.name == partner_language).get().id

            RuntimeStorageUser.time_zone = TimeZone.select(
                TimeZone.id).where(TimeZone.name == GeneralSettings.BOT_TIME_ZONE).get().id

            RuntimeStorageUser.currency = Currency.select(
                Currency.id).where(Currency.name == partner_currency).get().id

            RuntimeStorageUser.payment_info = Payment_info.select(Payment_info.id).where(
                Payment_info.card_number == partner_card_number).get().id

            RuntimeStorageUser.client_status = ClientStatus.select(
                ClientStatus.id).where(ClientStatus.name == partner_client_status).get().id

            RuntimeStorageUser.balance = 0
            RuntimeStorageUser.refund_balance = 0
            RuntimeStorageUser.client_orders_num = 0
            RuntimeStorageUser.client_disputs_percent = 0
            RuntimeStorageUser.client_total_sum = 0
            RuntimeStorageUser.solver = partner_solver

            RuntimeStorageUser.solver_status = SolverStatus.select(
                SolverStatus.id).where(SolverStatus.name == partner_solver_status).get().id

            RuntimeStorageUser.solver_orders_num = 0
            RuntimeStorageUser.solver_disputs_percent = 0
            RuntimeStorageUser.solver_total_sum = 0
            create_partner_user = User(telegram=RuntimeStorageUser.telegram,
                                       privileges=RuntimeStorageUser.privileges,
                                       language=RuntimeStorageUser.language,
                                       time_zone=RuntimeStorageUser.time_zone,
                                       currency=RuntimeStorageUser.currency,
                                       payment_info=RuntimeStorageUser.payment_info,
                                       client_status=RuntimeStorageUser.client_status,
                                       balance=RuntimeStorageUser.balance,
                                       refund_balance=RuntimeStorageUser.refund_balance,
                                       client_orders_num=RuntimeStorageUser.client_orders_num,
                                       client_disputs_percent=RuntimeStorageUser.client_disputs_percent,
                                       client_total_sum=RuntimeStorageUser.client_total_sum,
                                       solver=RuntimeStorageUser.solver,
                                       solver_status=RuntimeStorageUser.solver_status,
                                       solver_orders_num=RuntimeStorageUser.solver_orders_num,
                                       solver_disputs_percent=RuntimeStorageUser.solver_disputs_percent,
                                       solver_total_sum=RuntimeStorageUser.solver_total_sum)
            create_partner_user.save()

    def create_partner_source(self, partner_tg_id: int, partner_source_url: str,
                                partner_source_name: str, partner_source_country: str):
        with self.db:
            RuntimeStorageUser.telegram = Telegram.select(
                Telegram.id).where(Telegram.tg_id == partner_tg_id).get()
            RuntimeStorageUser.id = User.select(User.id).where(
                User.telegram == RuntimeStorageUser.telegram).get()
            
            create_partner_source = Source(partner_id=RuntimeStorageUser.id,
                                            source_url=partner_source_url,
                                            source_name=partner_source_name,
                                            source_num=0,
                                            source_state=0,
                                            replay_percent=0,
                                            diversity=0,
                                            total_orders=0,
                                            total_sum=0,
                                            country=partner_source_country)
            create_partner_source.save()