from typing import Any


class CheckOrderComplete:
    def __init__(self, order_id: int) -> None:
        self.order_id = order_id

    def get_order_subject_complete(self) -> Any:
        pass
    
    def get_order_topic_complete(self) -> Any:
        pass

    def get_order_comment_complete(self) -> Any:
        pass

    def get_order_files_complete(self) -> Any:
        pass

    def get_order_deadline_time_complete(self) -> Any:
        pass

    @property
    def check_all_order_settings(self) -> bool:
        subject_complete_value = self.get_order_subject_complete()
        topic_complete_value = self.get_order_topic_complete()
        comment_complete_value = self.get_order_comment_complete()
        files_complete_value = self.get_order_files_complete()
        deadline_time_complete_value = self.get_order_deadline_time_complete()

        all_order_values = (subject_complete_value,
                            topic_complete_value,
                            comment_complete_value,
                            files_complete_value,
                            deadline_time_complete_value)

        if all(item is not None for item in all_order_values):
            return True
        
        return False