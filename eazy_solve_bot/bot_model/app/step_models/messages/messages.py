from settings.views.messages.russian_messages import RussianMessages
from settings.views.messages.chinese_messages import ChineseMessages
from settings.views.messages.english_messages import EnglishMessages
from settings.views.messages.french_messages import FrenchMessages
from settings.views.messages.german_messages import GermanMessages
from settings.views.messages.spanish_messages import SpanishMessages
from settings.views.messages.portuguese_messages import PortugueseMessages
from settings.views.messages.ukrainian_messages import UkrainianMessages
from settings.views.messages.belarusian_messages import BelarusianMessages
from settings.views.messages.kazakh_messages import KazakhMessages
from settings.views.messages.georgian_messages import GeorgianMessages
from settings.views.messages.armenian_messages import ArmenianMessages
from settings.views.messages.hebrew_messages import HebrewMessages
from settings.views.messages.turkish_messages import TurkishMessages


LANGUAGES_MESSAGES = {"RUSSIAN": RussianMessages,
                        "CHINESE": ChineseMessages,
                        "ENGLISH": EnglishMessages,
                        "FRENCH": FrenchMessages,
                        "GERMAN": GermanMessages,
                        "SPANISH": SpanishMessages,
                        "PORTUGUESE": PortugueseMessages,
                        "UKRAINIAN": UkrainianMessages,
                        "BELARUSIAN": BelarusianMessages,
                        "KAZAKH": KazakhMessages,
                        "GEORGIAN": GeorgianMessages,
                        "ARMENIAN": ArmenianMessages,
                        "HEBREW": HebrewMessages,
                        "TURKISH": TurkishMessages}
class Messages:
    """"""
    BAD_SEND_ORDER_MESSAGE = "You haven't set all the required settings!"
    GET_ORDER_OTHER_TOPIC = "Please complete your subject in comments"
    def __init__(self, language: str) -> None:
        self.language = language
        #special
        self.MAIN_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].MAIN_MENU_MESSAGE
        self.BAD_USER_ANSWER_MESSAGE = LANGUAGES_MESSAGES[self.language].BAD_USER_ANSWER_MESSAGE
        #comands
        self.START_MESSAGE = LANGUAGES_MESSAGES[self.language].START_COMMAND_MESSAGE
        self.HELP_COMMAND_MESSAGE = LANGUAGES_MESSAGES[self.language].HELP_COMMAND_MESSAGE
        self.MAIN_MENU_COMMAND_MESSAGE = LANGUAGES_MESSAGES[self.language].MAIN_MENU_COMMAND_MESSAGE
        #first step
        self.CHECKING_USER_SUBSCRIPTION_MESSAGE = LANGUAGES_MESSAGES[self.language].CHECKING_USER_SUBSCRIPTION_MESSAGE
        self.CLIENT_MAIN_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].CLIENT_MAIN_MENU_MESSAGE
        self.CLIENT_AND_SOLVER_MAIN_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].CLIENT_AND_SOLVER_MAIN_MENU_MESSAGE
        self.PARTNER_MAIN_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].PARTNER_MAIN_MENU_MESSAGE
        self.ADMIN_MAIN_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].ADMIN_MAIN_MENU_MESSAGE
        self.ACCOUNTANT_MAIN_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].ACCOUNTANT_MAIN_MENU_MESSAGE
        self.CREATOR_MAIN_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].CREATOR_MAIN_MENU_MESSAGE

        self.PARTNER_CONTROL_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].PARTNER_CONTROL_MENU_MESSAGE
        self.ADMIN_CONTROL_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].ADMIN_CONTROL_MENU_MESSAGE
        self.ACCOUNTANT_CONTROL_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].ACCOUNTANT_CONTROL_MENU_MESSAGE
        self.CREATOR_CONTROL_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].CREATOR_CONTROL_MENU_MESSAGE
        #get language and time zone
        self.SETTING_UP_USER_LANGUAGE_MESSAGE = LANGUAGES_MESSAGES[self.language].SETTING_UP_USER_LANGUAGE_MESSAGE
        self.RESETTING_UP_USER_LANGUAGE_STEP = LANGUAGES_MESSAGES[self.language].RESETTING_UP_USER_LANGUAGE_STEP
        self.SETTING_UP_USER_TIME_ZONE_MESSAGE = LANGUAGES_MESSAGES[self.language].SETTING_UP_USER_TIME_ZONE_MESSAGE
        #main_menu
        self.NEW_ORDER_MESSAGE = LANGUAGES_MESSAGES[self.language].NEW_ORDER_MESSAGE
        self.ACTIVE_ORDERS_MESSAGE = LANGUAGES_MESSAGES[self.language].ACTIVE_ORDERS_MESSAGE
        self.MY_PROFILE_MESSAGE = LANGUAGES_MESSAGES[self.language].MY_PROFILE_MESSAGE
        self.BALANCE_MESSAGE = LANGUAGES_MESSAGES[self.language].BALANCE_MESSAGE
        self.SUPPORT_MESSAGE = LANGUAGES_MESSAGES[self.language].SUPPORT_MESSAGE
        self.REVIEWS_MESSAGE = LANGUAGES_MESSAGES[self.language].REVIEWS_MESSAGE
        self.AFFILIATE_PROGRAM_MESSAGE = LANGUAGES_MESSAGES[self.language].AFFILIATE_PROGRAM_MESSAGE
        self.SOLVER_MENU_MESSAGE = LANGUAGES_MESSAGES[self.language].SOLVER_MENU_MESSAGE
        #new order menu
        self.NEW_ORDER_BY_ADMIN_MESSAGE = LANGUAGES_MESSAGES[self.language].NEW_ORDER_BY_ADMIN_MESSAGE
        self.NEW_ORDER_BY_BOT_MESSAGE = LANGUAGES_MESSAGES[self.language].NEW_ORDER_BY_BOT_MESSAGE
        self.UNFINISHED_ORDER_MESSAGE = LANGUAGES_MESSAGES[self.language].UNFINISHED_ORDER_MESSAGE
        self.GET_ORDER_SETTINGS_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_SETTINGS_MESSAGE
        #
        self.GET_ORDER_SUBJECT_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_SUBJECT_MESSAGE
        self.GET_ORDER_COMMENT_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_COMMENT_MESSAGE
        self.GET_ORDER_FILES_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_FILES_MESSAGE
        self.GET_ORDER_DEADLINE_DATE_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_DEADLINE_DATE_MESSAGE
        self.GET_ORDER_DEADLINE_TIME_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_DEADLINE_TIME_MESSAGE
        self.GET_UP_ORDER_SETTINGS_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_UP_ORDER_SETTINGS_MESSAGE
        self.GET_ORDER_SUPPORT_DATE_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_SUPPORT_DATE_MESSAGE
        self.GET_ORDER_SUPPORT_TIME_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_SUPPORT_TIME_MESSAGE
        self.GET_ORDER_SUPPORT_COMMENT_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_SUPPORT_COMMENT_MESSAGE
        self.GET_ORDER_PERCENT_COMPLET_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_PERCENT_COMPLET_MESSAGE
        self.GET_ORDER_PREFERRED_BUDGET_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_PREFERRED_BUDGET_MESSAGE
        self.GET_ORDER_FORMAT_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_FORMAT_MESSAGE
        self.SEND_ORDER_TO_SOLVERS_MESSAGE = LANGUAGES_MESSAGES[self.language].SEND_ORDER_TO_SOLVERS_MESSAGE
        self.GET_ORDER_NUMBER_OF_TASKS_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_NUMBER_OF_TASKS_MESSAGE
        self.GET_ORDER_DURATION_TIME_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_DURATION_TIME_MESSAGE
        #
        self.GET_ORDER_TOPIC_MESSAGE = LANGUAGES_MESSAGES[self.language].GET_ORDER_TOPIC_MESSAGE
        #get order file messages
        self.ORDER_FILE_ADDED_MESSAGE = LANGUAGES_MESSAGES[self.language].ORDER_FILE_ADDED_MESSAGE
        self.ORDER_INVALID_FILE_MESSAGE = LANGUAGES_MESSAGES[self.language].ORDER_INVALID_FILE_MESSAGE
        self.EXCEEDED_THE_ALLOWED_LIMIT_OF_ORDER_FILES_MESSAGE = LANGUAGES_MESSAGES[self.language].EXCEEDED_THE_ALLOWED_LIMIT_OF_ORDER_FILES_MESSAGE
        self.DELETE_ALL_ORDER_FILES_MESSAGE = LANGUAGES_MESSAGES[self.language].DELETE_ALL_ORDER_FILES_MESSAGE

        #my profile menu
        self.SET_BANKING_DETAILS_MESSAGE = LANGUAGES_MESSAGES[self.language].SET_BANKING_DETAILS_MESSAGE
        self.SET_CURRENCY_MESSAGE = LANGUAGES_MESSAGES[self.language].SET_CURRENCY_MESSAGE
        self.SET_LANGUAGE_MESSAGE = LANGUAGES_MESSAGES[self.language].SET_LANGUAGE_MESSAGE
        #balance menu
        self.CASH_IN_MESSAGES = LANGUAGES_MESSAGES[self.language].CASH_IN_MESSAGES
        self.CASH_OUT_MESSAGES = LANGUAGES_MESSAGES[self.language].CASH_OUT_MESSAGES
        #support menu
        self.BECOME_A_PARTNER_MESSAGE = LANGUAGES_MESSAGES[self.language].BECOME_A_PARTNER_MESSAGE
        self.BECOME_A_SOLVER_MESSAGE = LANGUAGES_MESSAGES[self.language].BECOME_A_SOLVER_MESSAGE
        self.ASK_A_QUESTION_MESSAGE = LANGUAGES_MESSAGES[self.language].ASK_A_QUESTION_MESSAGE
        self.FAQ_MESSAGE = LANGUAGES_MESSAGES[self.language].FAQ_MESSAGE
        #affiliate program menu
        self.LIST_AFFILIATE_LINKS_MESSAGE = LANGUAGES_MESSAGES[self.language].LIST_AFFILIATE_LINKS_MESSAGE
        self.CREATE_AFFILIATE_LINK_MESSAGE = LANGUAGES_MESSAGES[self.language].CREATE_AFFILIATE_LINK_MESSAGE
        self.AFFILIATE_PROGRAM_STATISTICS_MESSAGE = LANGUAGES_MESSAGES[self.language].AFFILIATE_PROGRAM_STATISTICS_MESSAGE