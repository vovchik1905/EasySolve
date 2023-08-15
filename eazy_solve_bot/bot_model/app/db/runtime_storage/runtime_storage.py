from typing import Any

class RuntimeStorage:
    id: int

class RuntimeStorageClientStatus(RuntimeStorage):
    name: str

class RuntimeStorageSolverStatus(RuntimeStorage):
    name: str

class RuntimeStorageOrderFormat(RuntimeStorage):
    name: str

class RuntimeStorageOrderState(RuntimeStorage):
    name: str

class RuntimeStorageOrderImportance(RuntimeStorage):
    name: str

class RuntimeStorageLanguage(RuntimeStorage):
    name: str

class RuntimeStorageTelegram(RuntimeStorage):
    tg_id: int
    tg_name: str
    tg_sername: str
    tg_username: str

class RuntimeStorageCurrency(RuntimeStorage):
    name: str
    exchange_rate: float

class RuntimeStoragePayment_info(RuntimeStorage):
    card_number: str
    card_bank: str
    card_phone: str
    cardholler_name: str

class RuntimeStorageTimeZone(RuntimeStorage):
    name: str
    time_difference: int

class RuntimeStorageUser(RuntimeStorage):
    telegram: int
    privileges: int
    language: int
    time_zone: int
    currency: int
    payment_info: int
    client_status: int
    balance: int
    refund_balance: int
    client_orders_num: int
    client_disputs_percent: int
    client_total_sum: int
    solver: bool
    solver_status: int
    solver_orders_num: int
    solver_disputs_percent: int
    solver_total_sum: int

class RuntimeStorageClientReview(RuntimeStorage):
    for_user_id: int
    from_user_id: int
    client_review: str
    review_chat_id: int

class RuntimeStorageSolverReview(RuntimeStorage):
    for_user_id: int
    from_user_id: int
    client_review: str
    review_chat_id: int

class RuntimeStorageSource(RuntimeStorage):
    partner_id: int
    source_name: str
    source_num: int
    source_state: float
    replay_percent: float
    diversity: int
    total_orders: int
    total_sum: float
    country: str

class RuntimeStorageSource_User(RuntimeStorage):
    source_id: int
    user_id: int

class RuntimeStorageFile(RuntimeStorage):
    order: int
    file: str

class RuntimeStorageOrder(RuntimeStorage):
    user_id: int
    status: int
    format: int
    subject: str
    topic: str
    percent_complet: int
    deadline_time: Any
    preferred_budget: int
    comment: str
    importance: int
    support: bool
    time_support: Any
    support_comment: str

class RuntimeStorageOrderChange(RuntimeStorage):
    Order: int
    date_time_change: Any

class RuntimeStorageChat(RuntimeStorage):
    chat_id: int
    order_id: int

class RuntimeStorageOrder_User(RuntimeStorage):
    order_id: int
    solver_id: int

class RuntimeStorageOrderStateTime(RuntimeStorage):
    order_id: int
    order_status_id: int
    status_time_complete: Any