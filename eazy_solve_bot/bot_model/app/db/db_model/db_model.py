from peewee import *
from enum import IntEnum
import uuid
from settings.private.db_config.db_config import DbConfig


db = PostgresqlDatabase(database=DbConfig.DATABAZE,
                        user=DbConfig.USER,
                        password=DbConfig.PASSWORD,
                        host=DbConfig.HOST,
                        port=DbConfig.PORT)


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order = 'id'


class ClientStatus(BaseModel):
    name = CharField()#Наименование статуса клиента
    class Meta:
        db_table = 'ClientStatus'


class SolverStatus(BaseModel):
    name = CharField()#Наименование статуса исполнителя
    class Meta:
        db_table = 'SolverStatus'


class OrderFormat(BaseModel):
    name = CharField()#Наименование формата заказа
    class Meta:
        db_table = 'OrderFormat'


class OrderState(BaseModel):
    name = CharField()#Наименование состояния заказа
    class Meta:
        db_table = 'OrderState'


class OrderImportance(BaseModel):
    name = CharField()#Наименование важности заказа
    class Meta:
        db_table = 'OrderImportance'


class Language(BaseModel):
    name = CharField()
    class Meta:
        db_table = 'Languages'


class Telegram(BaseModel):
    tg_id = IntegerField()
    tg_name = CharField(default=None, null=True)
    tg_sername = CharField(default=None, null=True)
    tg_username = CharField(default=None, null=True)
    class Meta:
        db_table = 'Telegram'


class Currency(BaseModel):  # вылюта
    name = CharField(null = True)
    exchange_rate = FloatField(null=True, constraints=[Check('exchange_rate >= 0')])  # курс к рублю
    class Meta:
        db_table = 'Currencys'


class Payment_info(BaseModel):  # реквизиты клиента
    card_number = CharField(null=True)
    card_bank = CharField(null=True)
    card_phone = CharField(null=True)
    cardholler_name = CharField(null=True)
    class Meta:
        db_table = 'PaymentInfo'


class TimeZone(BaseModel):
    name = CharField()
    time_difference = IntegerField()
    class Meta:
        db_table = 'TimeZone'


class User(BaseModel):
    telegram = ForeignKeyField(Telegram)  # инфо-телега(1)
    privileges = IntegerField() #привелегия user(1)
    language = ForeignKeyField(Language)  # язык(2)
    time_zone = ForeignKeyField(TimeZone)
    currency = ForeignKeyField(Currency)  # валюта(3)
    payment_info = ForeignKeyField(Payment_info)  # платёжка(4)
    client_status = ForeignKeyField(ClientStatus)  # статус(1)
    balance = IntegerField(default=0, constraints=[Check('balance >= 0')])  # баланс
    refund_balance = IntegerField(default=0, constraints=[Check('refund_balance >= 0')])  # баланс затребованный в диспуте(висит пока не закончится диспут)
    #--------------------------------------------------
    client_orders_num = IntegerField(default=0, constraints=[Check('client_orders_num >= 0')])  # общее кол-во заказов
    client_disputs_percent = IntegerField(default=0, constraints=[Check('client_disputs_percent >= 0')])  # процент открытых диспутов от общего кол-во заказов
    client_total_sum = IntegerField(default=0, constraints=[Check('client_total_sum >= 0')])  # Общая сумма денег, которые клиент заплатил за заказы
    #--------------------------------------------------
    solver = BooleanField() # Является ли user исполнителем
    solver_status = ForeignKeyField(SolverStatus) #Статус исполнителя
    solver_orders_num = IntegerField(null=True, default=0, constraints=[Check('solver_orders_num >= 0')])  # общее кол-во выполненных заказов
    solver_disputs_percent = IntegerField(null=True, default=0, constraints=[Check('solver_disputs_percent >= 0')])  # процент открытых диспутов от общего кол-во выполненных заказов
    solver_total_sum = IntegerField(null=True, default=0, constraints=[Check('solver_total_sum >= 0')])  # Общая сумма денег, которые исполнитель получил за заказы
    class Meta:
        db_table = 'Users'


class ClientReview(BaseModel):  # отзывы про клиента
    for_user_id = ForeignKeyField(User)
    from_user_id = ForeignKeyField(User)
    client_review = TextField()
    review_chat_id = IntegerField()
    class Meta:
        db_table = 'ClientReviews'


class SolverReview(BaseModel): # отзывы про решателя
    for_user_id = ForeignKeyField(User)
    from_user_id = ForeignKeyField(User)
    solver_review = TextField()
    review_chat_id = IntegerField()
    class Meta:
        db_table = 'SolverReviews'


class Source(BaseModel):
    partner_id = ForeignKeyField(User)
    source_url = CharField()    #ссылка источника
    source_name = CharField()  # наименование источника
    source_num = IntegerField(default=0, constraints=[Check('source_num >= 0')])  # количество человек из источника
    source_state = FloatField(default=0, constraints=[Check('source_state >= 0')])  # статус источника
    replay_percent = FloatField(default=0, constraints=[Check('replay_percent >= 0')])  # процент людей сделавших более 1 заказа из этого источника
    diversity = IntegerField(default=0, constraints=[Check('diversity >= 0')])  # количество разных (качественно) заказов из этого источника
    total_orders = IntegerField(default=0, constraints=[Check('total_orders >= 0')])  # общее кол-во заказов из этого источника
    total_sum = FloatField(default=0, constraints=[Check('total_sum >= 0')])  # общая сумма оборота в рублях полученная от этого источника
    country = CharField(default="Москва")  # страна\место (привалирующая) из которой этот источник
    class Meta:
        db_table = 'Sources'


class Source_User(BaseModel):
    source_id = ForeignKeyField(Source)# Id источника
    user_id = ForeignKeyField(User)
    class Meta:
        db_table = 'SourcesUsers'


class OrderSubject(BaseModel):#new create
    name = CharField()
    class Meta:
        db_table = 'OrderSubjects'


class OrderTopic(BaseModel):
    name = CharField()
    class Meta:
        db_table = 'OrderTopics'


class Order(BaseModel):
    user_id = ForeignKeyField(User)
    status = ForeignKeyField(OrderState)  # статус заказа
    format = ForeignKeyField(OrderFormat)  # формат заказа
    subject = ForeignKeyField(OrderSubject)  # предметная область заказа
    topic = ForeignKeyField(OrderTopic)  # подраздел предметной области
    percent_complet = IntegerField(null=True, default=None, constraints=[Check('percent_complet >= 0')])  # минимальный процент на который необходимо выполнить заказ
    start_date = DateField(null=True, default=None)  #
    start_time = TimeField(null=True, default=None)  # начало заказа
    deadline_date = DateField(null=True, default=None)
    deadline_time = TimeField(null=True, default=None)  # дэдлайн заказа
    preferred_budget = IntegerField(null=True, constraints=[Check('preferred_budget >= 0')])  # предпочитаемый бюджет от заказчика
    comment = CharField(null=True, default=None)  # комментарий к заказу
    importance = ForeignKeyField(OrderImportance) #Важность заказа
    number_of_tasks = IntegerField(null=True)       #количество заданий
    duration_time = TimeField(null=True, default=None)        #продолжительность заказа
    support = BooleanField(null=True, default=False)  # есть ли поддержка работы (детали необходимо указать в комменте)
    #time_support = DateTimeField(null=True, default=None)  # время до которого требуется поддержка
    support_date = DateField(null=True, default=None)
    support_time = TimeField(null=True, default=None)
    support_comment = CharField(null=True, default=None)  # комментарий к поддержке заказа

    class Meta:
        db_table = 'Orders'


class File(BaseModel):
    order_id = ForeignKeyField(Order)
    file_tg_id = CharField()
    file_name = CharField(null=True)
    file_format = CharField(null=True)   #Формат файла
    file_datetime_get = DateTimeField(null=True, default=None)
    
    class Meta:
        db_table = 'Files'


class OrderChange(BaseModel):  # пользователь редактирует заказ
    Order = ForeignKeyField(Order)  # изменяемый заказ
    date_time_change = DateTimeField()  # время изменения заказа
    
    class Meta:
        db_table = 'OrderChanges'


#---------------------------------------------------------
class Chat(BaseModel):
    chat_id = IntegerField()
    order_id = ForeignKeyField(Order)
    class Meta:
        db_table = 'Chats'


class Order_User(BaseModel):
    #id = AutoField(primary_key=True, default=uuid.uuid4)
    order_id = ForeignKeyField(Order)
    solver_id = ForeignKeyField(User)
    class Meta:
        db_table = 'OrdersUsers'


class OrderStateTime(BaseModel):
    order_id = ForeignKeyField(Order)
    order_status_id = ForeignKeyField(OrderState)
    status_time_complete = DateTimeField(null=True, default=None)
    class Meta:
        db_table = 'OrderStateTime'
    #created_status_time = DateTimeField(null=True, default=None)
    #frozen_status_time = DateTimeField(null=True, default=None)
    #new_status_time = DateTimeField(null=True, default=None)
    #response_status_time = DateTimeField(null=True, default=None)
    #paid_status_time = DateTimeField(null=True, default=None)
    #in_process_status_time = DateTimeField(null=True, default=None)
    #cancel_status_time = DateTimeField(null=True, default=None)
    #in_disput_status_time = DateTimeField(null=True, default=None)
    #in_support_status_time = DateTimeField(null=True, default=None)
    #completed_status_time = DateTimeField(null=True, default=None)


"""
class UserLogs(BaseModel):
    user_id = ForeignKeyField(User)
    reg_time = DateTimeField(null=True, default=None)

"""