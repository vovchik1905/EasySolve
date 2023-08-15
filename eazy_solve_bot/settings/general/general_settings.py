import datetime
from settings.private.admin_config.admin_config import AdminConfig
from settings.private.admin_config.admin_paiment_info import AdminPaimentInfo
from settings.private.channel_config.channel_config import ChannelConfig


class GeneralSettings:
    """Initial settings:
        1)SUBSCRIBE_TO_THE_CHANNEL = True.

        2)LANGUAGES: "RUSSIAN": True, "ENGLISH": True && "ANY": False. 

        3)CURRENCY: "RUB": True && "ANY": False.

        4)CLIENT_STATUS_SETTINGS = ["NONE", "BAN", "BAD", "NEW", "SILVER", "GOLD", "PLATINUM", "VIP"]

        5)CLIENT_STATUS_THRESHOLD = {"BAD": (0, 0, 40), "NEW": (3, 3000, 30),
                                    "SILVER": (6, 6000, 50), "GOLD": (0, 0, 50),
                                    "PLATINUM": (0, 0, 100), "VIP": (0, 0, 100)}
    """

    SUBSCRIBE_TO_THE_CHANNEL = True

    GET_CLIENT_TIME_ZONE = True

    BOT_TIME_ZONE = "UTC+03"                   #UTC time zone

    """Language settings:"""
    LANGUAGES = {"RUSSIAN": True, "CHINESE": True,
                 "ENGLISH": True, "FRENCH": True,
                 "GERMAN": True, "SPANISH": True,
                 "PORTUGUESE": True, "UKRAINIAN": True,
                 "GEORGIAN": True, "ARMENIAN": True,
                 "HEBREW": True, "TURKISH": True
                 }

    """Currencys settings:"""
    CURRENCY = {"RUB": True, "CNY": True,
                "USD": True, "EUR": True,
                "UAH": True, "BYN": True,
                "KZT": True, "GEL": True,
                "AMD": True, "ILS": True,
                "TRY": True, "BTC": True,
                "USDT": True}
    
    TIME_ZONES = {"UTC-12": -12, "UTC-11": -11,
                    "UTC-10": -10, "UTC-09": -9,
                    "UTC-08": -8, "UTC-07": -7,
                    "UTC-06": -6, "UTC-05": -5,
                    "UTC-04": -4, "UTC-03": -3,
                    "UTC-02": -2, "UTC-01": -1,
                    "UTC+00": 0, "UTC+01": 1, 
                    "UTC+02": 2, "UTC+03": 3,
                    "UTC+04": 4, "UTC+05": 5,
                    "UTC+06": 6, "UTC+07": 7,
                    "UTC+08": 8, "UTC+09": 9,
                    "UTC+10": 10, "UTC+11": 11,
                    "UTC+12": 12, "UTC+13": 13}

    USER_PRIVILEGES_SETTINGS = [
        "CLIENT", "CLIENT_AND_SOLVER", "PARTNER", "ADMIN", "CREATOR"]

    """Bot client status:"""
    CLIENT_STATUS_SETTINGS = ["NONE", "BAN", "BAD",
                              "NEW", "SILVER", "GOLD", "PLATINUM", "VIP"]

    """Conditions of client status (number of orders, total amount, percentage of disputes):"""
    CLIENT_STATUS_THRESHOLD = {"BAD": (0, 0, 100), "NEW": (0, 0, 100),
                               "SILVER": (0, 0, 100), "GOLD": (0, 0, 100),
                               "PLATINUM": (0, 0, 100), "VIP": (0, 0, 100)}

    """Bot solver status:"""
    SOLVER_STATUS_SETTINGS = ["NONE", "BAN", "BAD",
                              "NEW", "SILVER", "GOLD", "PLATINUM", "VIP"]

    """Conditions of client status(number of orders, total amount, percentage of disputes):"""
    SOLVER_STATUS_THRESHOLD = {"BAD": (0, 0, 100), "NEW": (0, 0, 100),
                               "SILVER": (0, 0, 100), "GOLD": (0, 0, 100),
                               "PLATINUM": (0, 0, 100), "VIP": (0, 0, 100)}

    """Order formats:"""
    ORDER_FORMAT_SETTINGS = ["NONE", "CONTROL", "HOMEWORK",
                             "EXAM", "LABA", "COURSEWORK", "DIPLOMA", "OTHER"]

    """Order importance"""
    ORDER_IMPORTANCE_SETTINGS = ["STANDARD", "NOW", "IMPORTANT", "VOLUMINOUS"]

    BASE_PAYMENT_INFO = {"card_number": "0000 0000 0000 0000", "card_bank": "CARD BANK",
                        "card_phone": "+70000000000", "cardholler_name": "CARDHOLLER NAME"}

    """Limit on the number of files in the order"""
    ORDER_FILES_QUANTITY_LIMIT = 1
#--------------------------------------------------------------------------------------

    CREATOR_SETTINGS = {"telegram": (AdminConfig.CREATOR_TG_ID,
                                    AdminConfig.CREATOR_TG_NAME,
                                    AdminConfig.CREATOR_TG_SERNAME,
                                    AdminConfig.CREATOR_TG_USERNAME),
                        "language": "RUSSIAN",
                        "currency": "RUB",
                        "payment_info": (AdminPaimentInfo.CREATOR_CARD_NUMBER,
                                        AdminPaimentInfo.CREATOR_CARD_BANK,
                                        AdminPaimentInfo.CREATOR_CARD_PHONE,
                                        AdminPaimentInfo.CREATOR_CARDHOLLER_NAME),
                        "privileges": 6,
                        "client_status": "VIP",
                        "solver": True,
                        "solver_status": "VIP"}

    ACCOUNTANT_SETTINGS = {"telegram": (AdminConfig.ACCOUNTANT_TG_ID,
                                        AdminConfig.ACCOUNTANT_TG_NAME,
                                        AdminConfig.ACCOUNTANT_TG_SERNAME,
                                        AdminConfig.ACCOUNTANT_TG_USERNAME),
                            "language": "RUSSIAN",
                            "currency": "RUB",
                            "payment_info": (AdminPaimentInfo.ACCOUNTANT_CARD_NUMBER,
                                            AdminPaimentInfo.ACCOUNTANT_CARD_BANK,
                                            AdminPaimentInfo.ACCOUNTANT_CARD_PHONE,
                                            AdminPaimentInfo.ACCOUNTANT_CARDHOLLER_NAME),
                            "privileges": 5,
                            "client_status": "PLATINUM",
                            "solver": True,
                            "solver_status": "PLATINUM"}

    ADMIN_SETTINGS = {"telegram": (AdminConfig.ADMIN_TG_ID,
                                    AdminConfig.ADMIN_TG_NAME,
                                    AdminConfig.ADMIN_TG_SERNAME,
                                    AdminConfig.ADMIN_TG_USERNAME),
                            "language": "RUSSIAN",
                            "currency": "RUB",
                            "payment_info": (AdminPaimentInfo.ADMIN_CARD_NUMBER,
                                            AdminPaimentInfo.ADMIN_CARD_BANK,
                                            AdminPaimentInfo.ADMIN_CARD_PHONE,
                                            AdminPaimentInfo.ADMIN_CARDHOLLER_NAME),
                            "privileges": 4,
                            "client_status": "PLATINUM",
                            "solver": True,
                            "solver_status": "PLATINUM"}

    PARTNER_SETTINGS = {"telegram": (AdminConfig.PARTNER_TG_ID,
                                    AdminConfig.PARTNER_TG_NAME,
                                    AdminConfig.PARTNER_TG_SERNAME,
                                    AdminConfig.PARTNER_TG_USERNAME),
                        "language": "RUSSIAN",
                        "currency": "RUB",
                        "payment_info": (AdminPaimentInfo.PARTNER_CARD_NUMBER,
                                        AdminPaimentInfo.PARTNER_CARD_BANK,
                                        AdminPaimentInfo.PARTNER_CARD_PHONE,
                                        AdminPaimentInfo.PARTNER_CARDHOLLER_NAME),
                        "privileges": 3,
                        "client_status": "PLATINUM",
                        "solver": True,
                        "solver_status": "PLATINUM"}
    

    MAIN_SOURCE_SETTINGS = {"tg_id": AdminConfig.PARTNER_TG_ID,
                            "url": ChannelConfig.CHANNEL_URL,
                            "name": ChannelConfig.CHANNEL_NAME,
                            "country": ChannelConfig.CHANNEL_COUNTRY}


    DATE_YEAR = datetime.datetime.today().year

    DATE_MONTH = datetime.datetime.today().month

    DATE_DAY = datetime.datetime.today().day