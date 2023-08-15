from enum import Enum

class OrderSubject(Enum):
    NONE_SBJ = "NONE"
    MATHS_SBJ = "MATHS"
    PHYSICS_SBJ = "PHYSICS"
    IT_SBJ = "IT"
    ENGINEERING_SBJ = "ENGINEERING"
    ECONOMY_SBJ = "ECONOMY"
    CHEMISTRY_SBJ = "CHEMISTRY"
    LANGUAGES_SBJ = "LANGUAGES"
    BIOLOGY_SBJ = "BIOLOGY"
    GEOGRAPHY_SBJ = "GEOGRAPHY"
    HUMANITARIAN_SBJ = "HUMANITARIAN"
    REGISTRATION = "REGISTRATION"
    OTHER_SBJ = "OTHER"


ORDER_SUBJECT = {"NONE": OrderSubject.NONE_SBJ,
                "MATHS": OrderSubject.MATHS_SBJ,
                "PHYSICS": OrderSubject.PHYSICS_SBJ,
                "IT": OrderSubject.IT_SBJ,
                "ENGINEERING": OrderSubject.ENGINEERING_SBJ,
                "ECONOMY": OrderSubject.ECONOMY_SBJ,
                "CHEMISTRY": OrderSubject.CHEMISTRY_SBJ,
                "LANGUAGES": OrderSubject.LANGUAGES_SBJ,
                "BIOLOGY": OrderSubject.BIOLOGY_SBJ,
                "GEOGRAPHY": OrderSubject.GEOGRAPHY_SBJ,
                "HUMANITARIAN": OrderSubject.HUMANITARIAN_SBJ,
                "REGISTRATION": OrderSubject.REGISTRATION,
                "OTHER": OrderSubject.OTHER_SBJ}