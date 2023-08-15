from enum import IntEnum


class OrderFormatEnum(IntEnum):
    NONE = 1
    CONTROL = 2
    HOMEWORK = 3
    EXAM = 4
    LABA = 5
    COURSEWORK = 6
    DIPLOMA = 7
    OTHER = 8


ORDER_FORMAT = {"NONE": OrderFormatEnum.NONE,
                "CONTROL": OrderFormatEnum.CONTROL,
                "HOMEWORK": OrderFormatEnum.HOMEWORK,
                "EXAM": OrderFormatEnum.EXAM,
                "LABA": OrderFormatEnum.LABA,
                "COURSEWORK": OrderFormatEnum.COURSEWORK,
                "DIPLOMA": OrderFormatEnum.DIPLOMA,
                "OTHER": OrderFormatEnum.OTHER}