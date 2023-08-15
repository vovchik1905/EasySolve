from typing import Any
from bot_model.app.db.db_model.db_model import ClientStatus, SolverStatus,\
    OrderFormat, OrderState, OrderImportance, Language, Telegram, Currency,\
        Payment_info, User, ClientReview, SolverReview, Source, Source_User,\
            File, OrderSubject, OrderTopic, Order, OrderChange, Chat, Order_User, db


class FileRequests:
    
    def __init__(self, db) -> None:
        self.db = db
    
    def create_file(self, order_id: int, file_tg_id: str,
                    file_name: str = None, file_format: str = None, file_datetime_get = None) -> None:
        with self.db:
            create_file = File(order_id=order_id,
                                file_tg_id=file_tg_id,
                                file_name=file_name,
                                file_format=file_format,
                                file_datetime_get=file_datetime_get)
            create_file.save()

    def get_all_order_files(self, file_order_id: int) -> list:
        if file_order_id is None:
            return None
        files_data = []
        with self.db:
            files_query = File.select().where(File.order_id == file_order_id)
            for file in files_query:
                files_data.append((file.file_tg_id, file.file_name, file.file_format))
        if not files_data:
            return None
        return files_data

    def get_order_files_num(self, order_id: int) -> int:
        with self.db:
            files_query = File.select().where(File.order_id == order_id)
            if files_query is None:
                return 0
            return files_query.count()
    
    def delete_all_order_files(self, order_id: int) -> None:
        with self.db:
            delete_files_query = File.delete().where(File.order_id == order_id)
            delete_files_query.execute()


file_request = FileRequests(db)