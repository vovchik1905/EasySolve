#from typing import Any
#from settings.general.order_subject import ORDER_SUBJECT, OrderSubject
#from settings.general.order_topic import ORDER_TOPIC, OrderTopic
#from bot_model.app.db.requests.order_request import order_request
#from bot_model.app.db.requests.file_requests import file_request
#
#
#class CheckOrderComplete:
#    def __init__(self, order_id: int) -> None:
#        self.order_id = order_id
#
#    def get_order_subject_complete(self) -> Any:
#        order_subject = order_request.get_order_subject_name(self.order_id)
#        if order_subject is None or ORDER_SUBJECT[order_subject] is OrderSubject.NONE_SBJ:
#            return None
#        else:
#            return order_subject
#    
#    def get_order_topic_complete(self) -> Any:
#        order_topic = order_request.get_order_topic_name(self.order_id)
#        if order_topic is None or ORDER_TOPIC[order_topic] is OrderTopic.NONE_TOPIC:
#            return None
#        return order_topic
#
#    def get_order_comment_complete(self) -> Any:
#        order_comment = order_request.get_order_comment(self.order_id)
#        if order_comment is None:
#            return None
#        return order_comment
#
#    def get_order_files_complete(self) -> Any:
#        order_files = file_request.get_all_order_files(self.order_id)
#        if order_files is None:
#            return None
#        return order_files
#
#    def get_order_deadline_time_complete(self) -> Any:
#        order_deadline_time = order_request.get_order_deadline_time(self.order_id)
#        if order_deadline_time is None:
#            return None
#        return order_deadline_time
#
#    def check_all_order_settings(self) -> bool:
#        subject_complete_value = self.get_order_subject_complete()
#        topic_complete_value = self.get_order_topic_complete()
#        comment_complete_value = self.get_order_comment_complete()
#        files_complete_value = self.get_order_files_complete()
#        deadline_time_complete_value = self.get_order_deadline_time_complete()
#
#        all_order_values = (subject_complete_value,
#                            topic_complete_value,
#                            comment_complete_value,
#                            files_complete_value,
#                            deadline_time_complete_value)
#
#        if all(item is not None for item in all_order_values):
#            return True
#        
#        return False