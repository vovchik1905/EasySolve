from enum import IntEnum

class OrderStateEnum(IntEnum):
    ORDER_CREATED = 1 # Заказ создаётся
    ORDER_FROZEN = 2
    NEW_ORDER = 3  # Заказ принят
    ORDER_RESPONSE = 4  # Откликнулись решатели
    ORDER_PAID = 5  # Заказ оплачен
    ORDER_IN_PROCESS = 6  # Заказ выполняется
    ORDER_CANCEL = 7  # Заказ отменен
    ORDER_IN_DISPUT = 8  # Диспут по заказу
    ORDER_IN_SUPPORT = 9  # Заказ сопровождается
    ORDER_COMPLETED = 10  # Заказ завершён


ORDER_STATE = {"ORDER_CREATED": OrderStateEnum.ORDER_CREATED,
                "ORDER_FROZEN": OrderStateEnum.ORDER_FROZEN,
                "NEW_ORDER": OrderStateEnum.NEW_ORDER,
                "ORDER_RESPONSE": OrderStateEnum.ORDER_RESPONSE,
                "ORDER_PAID": OrderStateEnum.ORDER_PAID,
                "ORDER_IN_PROCESS": OrderStateEnum.ORDER_IN_PROCESS,
                "ORDER_CANCEL": OrderStateEnum.ORDER_CANCEL,
                "ORDER_IN_DISPUT": OrderStateEnum.ORDER_IN_DISPUT,
                "ORDER_IN_SUPPORT": OrderStateEnum.ORDER_IN_SUPPORT,
                "ORDER_COMPLETED": OrderStateEnum.ORDER_COMPLETED}

STATE_ORDER = {OrderStateEnum.ORDER_CREATED: "ORDER_CREATED",
                OrderStateEnum.ORDER_FROZEN: "ORDER_FROZEN",
                OrderStateEnum.NEW_ORDER: "NEW_ORDER",
                OrderStateEnum.ORDER_RESPONSE: "ORDER_RESPONSE",
                OrderStateEnum.ORDER_PAID: "ORDER_PAID",
                OrderStateEnum.ORDER_IN_PROCESS: "ORDER_IN_PROCESS",
                OrderStateEnum.ORDER_CANCEL: "ORDER_CANCEL",
                OrderStateEnum.ORDER_IN_DISPUT: "ORDER_IN_DISPUT",
                OrderStateEnum.ORDER_IN_SUPPORT: "ORDER_IN_SUPPORT",
                OrderStateEnum.ORDER_COMPLETED: "ORDER_COMPLETED"}