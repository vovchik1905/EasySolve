import datetime
from typing import Any
from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, OrderSubject, OrderTopic, Order, OrderChange, Chat, Order_User, db

from bot_model.app.db.requests.telegram_requests import TelegramRequests, telegram_request
from bot_model.app.db.requests.user_requests import UserRequests, user_request
from bot_model.app.db.requests.language_requests import LanguageRequests, language_request
from settings.general.order_state import STATE_ORDER, OrderStateEnum


class OrderRequests:
    def __init__(self, db) -> None:
        self.db = db
    
    def create_order(self, order_user_id: int, order_importance: int, order_format: int = 1,
                    order_status: int = 1, order_subject: int = 1, order_topic: int = 1) -> None:
        #order_status_id = OrderState.select(OrderState.id).where(OrderState.name == STATE_ORDER[OrderStateEnum.ORDER_CREATED]).get().id
        create_order = Order(user_id=order_user_id,
                            format=order_format,
                            status=order_status,
                            subject=order_subject,
                            topic=order_topic,
                            importance = order_importance)
        create_order.save()
    
    def update_order_status(self, order_id: int, order_status: int) -> None:
        update_order_status = Order.get(Order.id==order_id)
        update_order_status.status = order_status
        update_order_status.save()

    def update_order_format(self, order_id: int, order_format: int) -> None:
        update_order_format = Order.get(Order.id==order_id)
        update_order_format.format = order_format
        update_order_format.save()
    
    def update_order_subject(self, order_id: int, order_subject: int) -> None:
        update_order_subject = Order.get(Order.id==order_id)
        update_order_subject.subject = order_subject
        update_order_subject.save()
    
    def update_order_topic(self, order_id: int, order_topic: int) -> None:
        update_order_topic = Order.get(Order.id==order_id)
        update_order_topic.topic = order_topic
        update_order_topic.save()
    
    def update_order_percent_complet(self, order_id: int, order_percent_complet: int) -> None:
        update_order_percent_complet = Order.get(Order.id==order_id)
        update_order_percent_complet.percent_complet = order_percent_complet
        update_order_percent_complet.save()
    
    def update_order_start_date(self, order_id: int, order_start_date: tuple) -> None:
        start_year, start_month, start_day = order_start_date
        start_date = datetime.date(start_year, start_month, start_day)
        update_order_start_date = Order.get(Order.id==order_id)
        update_order_start_date.start_date = start_date
        #update_order_start_date.start_date.year = start_year
        #update_order_start_date.start_date.month = start_month
        #update_order_start_date.start_date.day = start_day
        update_order_start_date.save()

    def update_order_start_time(self, order_id: int, order_start_time: tuple) -> None:
        start_hour, start_minute, start_second = order_start_time
        update_order_start_time = Order.get(Order.id==order_id)
        start_time = datetime.time(start_hour, start_minute, start_second)
        update_order_start_time.start_time = start_time
        #update_order_start_time.start_time.hour = start_hour
        #update_order_start_time.start_time.minute = start_minute
        #update_order_start_time.start_time.second = start_second
        update_order_start_time.save()

    def update_order_deadline_date(self, order_id: int, order_deadline_date: tuple) -> None:
        deadline_year, deadline_month, deadline_day = order_deadline_date
        update_order_deadline_date = Order.get(Order.id==order_id)
        deadline_date = datetime.date(deadline_year, deadline_month, deadline_day)
        update_order_deadline_date.deadline_date = deadline_date
        #update_order_deadline_date.deadline_date.year = deadline_year
        #update_order_deadline_date.deadline_date.month = deadline_month
        #update_order_deadline_date.deadline_date.day = deadline_day
        update_order_deadline_date.save()

    def update_order_deadline_time(self, order_id: int, order_deadline_time: tuple) -> None:
        deadline_hour, deadline_minute, deadline_second = order_deadline_time
        update_order_deadline_time = Order.get(Order.id==order_id)
        deadline_time = datetime.time(deadline_hour, deadline_minute, deadline_second)
        update_order_deadline_time.deadline_time = deadline_time
        #update_order_deadline_time.deadline_time.hour = deadline_hour
        #update_order_deadline_time.deadline_time.minute = deadline_minute
        #update_order_deadline_time.deadline_time.second = deadline_second
        update_order_deadline_time.save()
    
    def update_order_preferred_budget(self, order_id: int, order_preferred_budget: int) -> None:
        update_order_preferred_budget = Order.get(Order.id==order_id)
        update_order_preferred_budget.preferred_budget = order_preferred_budget
        update_order_preferred_budget.save()
    
    def update_order_comment(self, order_id: int, order_comment: int) -> None:
        update_order_comment = Order.get(Order.id==order_id)
        update_order_comment.comment = order_comment
        update_order_comment.save()
    
    def update_order_importance(self, order_id: int, order_comment: int) -> None:
        update_order_importance = Order.get(Order.id==order_id)
        update_order_importance.importance = order_comment
        update_order_importance.save()
    
    def update_order_support(self, order_id: int, order_support: bool) -> None:
        update_order_support = Order.get(Order.id==order_id)
        update_order_support.support = order_support
        update_order_support.save()
    
    def update_order_support_date(self, order_id: int, order_support_date: tuple) -> None:
        deadline_year, deadline_month, deadline_day = order_support_date
        update_order_support_date = Order.get(Order.id==order_id)
        support_date = datetime.date(deadline_year, deadline_month, deadline_day)
        update_order_support_date.support_date = support_date
        update_order_support_date.save()
    
    def update_order_support_time(self, order_id: int, order_support_time: tuple) -> None:
        deadline_hour, deadline_minute, deadline_second = order_support_time
        update_support_time = Order.get(Order.id==order_id)
        support_time = datetime.time(deadline_hour, deadline_minute, deadline_second)
        update_support_time.support_time = support_time
        update_support_time.save()
    
    def update_order_support_comment(self, order_id: int, order_support_comment: int) -> None:
        update_order_support_comment = Order.get(Order.id==order_id)
        update_order_support_comment.support_comment = order_support_comment
        update_order_support_comment.save()
    
    def update_order_number_of_tasks(self, order_id: int, order_number_of_tasks: int) -> None:
        update_order_number_of_tasks = Order.get(Order.id==order_id)
        update_order_number_of_tasks.number_of_tasks = order_number_of_tasks
        update_order_number_of_tasks.save()

    def update_order_duration_time(self, order_id: int, order_duration_time: tuple) -> None:
        duration_hour, duration_minute, duration_second = order_duration_time
        update_order_duration_time = Order.get(Order.id==order_id)
        duration_time = datetime.time(duration_hour, duration_minute, duration_second)
        update_order_duration_time.duration_time = duration_time
        update_order_duration_time.save()
    
    def get_or_none_status_order_id_with_user_id(self, order_user_id: int, order_status) -> Any:
        created_orders_id = []
        with self.db:
            order_id = Order.get_or_none(user_id=order_user_id, status=order_status)
        return order_id
    
    def get_order_status(self, order_id: int) -> int:
        with self.db:
            order_status = Order.select(Order.status).where(Order.id == order_id).get().status
        return order_status
    
    def get_order_importance_id(self, importance_name: str) -> int:
        with self.db:
            order_format_id = OrderImportance.select(OrderImportance.id).where(OrderImportance.name == importance_name).get().id
        return order_format_id
    
    def get_order_subject_name(self, order_id: int) -> Any:
        if order_id is None:
            return None
        #дописать проверку на Null
        with self.db:
            order_subject_id = Order.select(Order.subject).where(Order.id == order_id).get().subject
            order_subject_name = OrderSubject.select(OrderSubject.name).where(OrderSubject.id == order_subject_id).get().name
        return order_subject_name
    
    def get_order_topic_name(self, order_id: int) -> Any:
        if order_id is None:
            return None
        with self.db:
            order_topic_id = Order.select(Order.topic).where(Order.id == order_id).get().topic
            order_topic_name = OrderTopic.select(OrderTopic.name).where(OrderTopic.id == order_topic_id).get().name
        return order_topic_name
    
    def get_order_comment(self, order_id: int) -> Any:
        if order_id is None:
            return None
        with self.db:
            order_comment = Order.select(Order.comment).where(Order.id == order_id).get().comment
        return order_comment
    
    def get_order_deadline_date(self, order_id: int) -> Any:
        if order_id is None:
            return None
        with self.db:
            order_deadline_date = Order.select(Order.deadline_date).where(Order.id == order_id).get().deadline_date
        return order_deadline_date
    
    def get_order_deadline_time(self, order_id: int) -> Any:
        if order_id is None:
            return None
        with self.db:
            order_deadline_time = Order.select(Order.deadline_time).where(Order.id == order_id).get().deadline_time
        return order_deadline_time
    
    def get_order_support(self, order_id: int) -> Any:
        if order_id is None:
            return None
        with self.db:
            order_support = Order.select(Order.support).where(Order.id == order_id).get().support
        return order_support

    def get_order_support_date(self, order_id: int) -> Any:
        if order_id is None:
            return None
        with self.db:
            order_support_date = Order.select(Order.support_date).where(Order.id == order_id).get().support_date
        return order_support_date
    
    def get_order_support_time(self, order_id: int) -> Any:
        if order_id is None:
            return None
        with self.db:
            order_support_time = Order.select(Order.support_time).where(Order.id == order_id).get().support_time
        return order_support_time
    
    def get_order_subject_id(self, order_subject_name: str) -> int:
        with self.db:
            order_subject_id = OrderSubject.select(OrderSubject.id).where(OrderSubject.name == order_subject_name).get().id
        return order_subject_id
    
    def get_order_topic_id(self, order_topic_name: str) -> int:
        with self.db:
            order_topic_id = OrderTopic.select(OrderTopic.id).where(OrderTopic.name == order_topic_name).get().id
        return order_topic_id
    
    def get_order_format_id(self, order_format_name: str) -> int:
        with self.db:
            order_format_id = OrderFormat.select(OrderFormat.id).where(OrderFormat.name == order_format_name).get().id
        return order_format_id
    
    def get_order_importance_name_with_order_id(self, order_id: int) -> str:
        if order_id is None:
            return None
        with self.db:
            order_importance_id = Order.select(Order.importance).where(Order.id == order_id).get().importance
            order_importance_name = OrderImportance.select(OrderImportance.name).where(OrderImportance.id == order_importance_id).get().name
        return order_importance_name
    
    def get_order_percent_complet(self, order_id: int) -> int:
        if order_id is None:
            return None
        with self.db:
            order_percent_complet = Order.select(Order.percent_complet).where(Order.id == order_id).get().percent_complet
        return order_percent_complet
    
    def get_order_preferred_budget(self, order_id: int) -> int:
        if order_id is None:
            return None
        with self.db:
            order_preferred_budget = Order.select(Order.preferred_budget).where(Order.id == order_id).get().preferred_budget
        return order_preferred_budget
    
    def get_order_format_name(self, order_id: int) -> str:
        if order_id is None:
            return None
        with self.db:
            order_format_id = Order.select(Order.format).where(Order.id == order_id).get().format
            order_format_name = OrderFormat.select(OrderFormat.name).where(OrderFormat.id == order_format_id).get().name
        return order_format_name
    
    def get_order_number_of_tasks(self, order_id: int) -> int:
        if order_id is None:
            return None
        with self.db:
            order_number_of_tasks = Order.select(Order.number_of_tasks).where(Order.id == order_id).get().number_of_tasks
        return order_number_of_tasks
    
    def get_order_duration_time(self, order_id: int) -> int:
        if order_id is None:
            return None
        with self.db:
            order_duration_time = Order.select(Order.duration_time).where(Order.id == order_id).get().duration_time
        return order_duration_time
    
    def get_all_fields(self, order_id: int) -> Any:
        if order_id is None:
            return None
        with self.db:
            all_order_fields = Order.select().where(Order.id == order_id).get()
            print(all_order_fields)
            return all_order_fields
            

order_request = OrderRequests(db)