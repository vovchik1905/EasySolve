from enum import IntEnum


class OrderImportanceEnum(IntEnum):
    STANDARD = 1
    NOW = 2
    IMPORTANT = 3
    VOLUMINOUS = 4


ORDER_IMPORTANCE = {"STANDARD": OrderImportanceEnum.STANDARD,
                    "NOW": OrderImportanceEnum.NOW,
                    "IMPORTANT": OrderImportanceEnum.IMPORTANT,
                    "VOLUMINOUS": OrderImportanceEnum.VOLUMINOUS}

IMPORTANCE_ORDER = {OrderImportanceEnum.STANDARD: "STANDARD",
                    OrderImportanceEnum.NOW: "NOW",
                    OrderImportanceEnum.IMPORTANT: "IMPORTANT",
                    OrderImportanceEnum.VOLUMINOUS: "VOLUMINOUS"}