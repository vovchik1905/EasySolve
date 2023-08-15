import datetime
from bot_model.app.step_models.messages.messages import Messages
from bot_model.app.step_models.keyboards.checking_user_subscription_menu import CheckingUserSubscriptionMenu
from bot_model.app.step_models.keyboards.client_main_menu import ClientMainMenuKeyboard
from bot_model.app.step_models.keyboards.client_and_solver_main_menu import ClientAndSolverMainMenuKeyboard
from bot_model.app.step_models.keyboards.partner_main_menu import PartnerMainMenuKeyboard
from bot_model.app.step_models.keyboards.admin_main_menu import AdminMainMenuKeyboard
from bot_model.app.step_models.keyboards.accountant_main_menu import AccountantMainMenuKeyboard
from bot_model.app.step_models.keyboards.creator_main_menu import CreatorMainMenuKeyboard
from bot_model.app.step_models.keyboards.languages_keyboard import LanguagesKeyboard
from bot_model.app.step_models.keyboards.support_menu import SupportMenuKeyboard
from bot_model.app.step_models.keyboards.support_faq_menu import SupportFaqMenuKeyboard
from bot_model.app.step_models.keyboards.back_menu import BackMenuKeyboard
from bot_model.app.step_models.keyboards.balance_menu import BalanceMenuKeyboard
from bot_model.app.step_models.keyboards.my_profile_menu import MyProfileMenuKeyboard
from bot_model.app.step_models.keyboards.affiliate_program_menu import AffiliateProgramMenuKeyboard
from bot_model.app.step_models.keyboards.new_order_menu import NewOrderMenuKeyboard
from bot_model.app.step_models.keyboards.order_importance_menu import OrderImportanceMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.main_standart_order_menu import MainStandartOrderMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.main_now_order_menu import MainNowOrderMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.main_important_order_menu import MainImportantOrderMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.main_voluminous_order_menu import MainVoluminousOrderMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.additional_order_settings_menu import AdditionalOrderSettingsMenuKeyboard
from bot_model.app.step_models.keyboards.time_zones_keyboard import TimeZoneKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.subjects_menu import SubjectMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.maths_topic_menu import MathsMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.physics_topic_menu import PhysicsMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.it_topic_menu import ITMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.engineering_topic_menu import EngineeringMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.economy_topic_menu import EconomyMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.chemistry_topic_menu import ChemistryMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.languages_topic_menu import LanguagesTopicMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.biology_topic_menu import BiologyTopicMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.geography_topic_menu import GeographyTopicMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.humanitarian_topic_menu import HumanitarianTopicMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.subjects_keyboards.registration_topic_menu import RegistrationTopicMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.deadline_time_keyboards.get_data_keyboard import GetDateMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.deadline_time_keyboards.get_time_keyboard import GetTimeMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.get_files_menu import GetOrderFilesMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.get_order_format_menu import GetOrderFormatMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.get_order_percent_complet_menu import GetOrderPercentCompleteMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.deadline_time_keyboards.get_order_duration_keyboard import GetDurationMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.check_order_complite_keyboard import CheckOrderCompliteMenu
from bot_model.app.db.requests.order_request import order_request


class Views:
    def __init__(self, language: str, tg_id: int, order_id: int = None) -> None:
        self.language = language
        self.tg_id = tg_id
        self.order_id = order_id
        
        message_object = Messages(self.language)
        back_menu = BackMenuKeyboard(self.language)
        checking_user_subscription_menu = CheckingUserSubscriptionMenu(self.language)
        self.client_main_menu = ClientMainMenuKeyboard(self.language, self.tg_id)
        self.client_and_solver_main_menu = ClientAndSolverMainMenuKeyboard(self.language, self.tg_id)
        partner_main_menu = PartnerMainMenuKeyboard(self.language)
        admin_main_menu = AdminMainMenuKeyboard(self.language)
        accountant_main_menu = AccountantMainMenuKeyboard(self.language)
        creator_main_menu = CreatorMainMenuKeyboard(self.language)
        languages_kb = LanguagesKeyboard(self.language)
        time_zone_kb = TimeZoneKeyboard(self.language)
        support_kb = SupportMenuKeyboard(self.language)
        support_faq_kb = SupportFaqMenuKeyboard(self.language)
        balance_menu = BalanceMenuKeyboard(self.language)
        my_profile_menu = MyProfileMenuKeyboard(self.language)
        affiliate_program_menu = AffiliateProgramMenuKeyboard(self.language)
        new_order_menu = NewOrderMenuKeyboard(self.language, self.tg_id)
        order_importance_menu = OrderImportanceMenuKeyboard(self.language, self.tg_id)
        main_standart_order_menu = MainStandartOrderMenuKeyboard(self.language, self.order_id)
        main_now_order_menu = MainNowOrderMenuKeyboard(self.language, self.order_id)
        main_important_order_menu = MainImportantOrderMenuKeyboard(self.language, self.order_id)
        main_voluminous_order_menu = MainVoluminousOrderMenuKeyboard(self.language, self.order_id)
        additional_order_settings_menu = AdditionalOrderSettingsMenuKeyboard(self.language, self.order_id)
        get_order_files_menu = GetOrderFilesMenuKeyboard(self.language, self.order_id)
        subject_menu = SubjectMenuKeyboard(self.language)
        maths_topics_menu = MathsMenuKeyboard(self.language)
        physics_topics_menu = PhysicsMenuKeyboard(self.language)
        it_topics_menu = ITMenuKeyboard(self.language)
        engineering_topics_menu = EngineeringMenuKeyboard(self.language)
        economy_topics_menu = EconomyMenuKeyboard(self.language)
        chemistry_topics_menu = ChemistryMenuKeyboard(self.language)
        languages_topics_menu = LanguagesTopicMenuKeyboard(self.language)
        biology_topics_menu = BiologyTopicMenuKeyboard(self.language)
        geography_topics_menu = GeographyTopicMenuKeyboard(self.language)
        humanitarian_topics_menu = HumanitarianTopicMenuKeyboard(self.language)
        registration_topics_menu = RegistrationTopicMenuKeyboard(self.language)
        check_order_complite_menu = CheckOrderCompliteMenu(self.language)

        if order_id is not None:
            order_deadline_date = order_request.get_order_deadline_date(order_id)
            #order_deadline_date = order_request.get_order_support_date(order_id)
            if order_deadline_date is None:
                year = int(datetime.datetime.today().year)
                month = int(datetime.datetime.today().month)
                day = int(datetime.datetime.today().day)
            else:
                year = int(order_deadline_date.year)
                month = int(order_deadline_date.month)
                print(year, month)
                if month == datetime.datetime.today().month:
                    day = int(datetime.datetime.today().day)
                else:
                    day = 1
                    #day = int(order_deadline_date.day)
        else:
            year = int(datetime.datetime.today().year)
            month = int(datetime.datetime.today().month)
            day = int(datetime.datetime.today().day)
        get_date_keyboard = GetDateMenuKeyboard(self.language, year, month, day)

        get_time_keyboard = GetTimeMenuKeyboard(self.language)

        get_order_format_keyboard = GetOrderFormatMenuKeyboard(self.language, self.order_id)

        if order_id is not None:
            order_support_deadline_date = order_request.get_order_support_date(order_id)
            #order_support_deadline_date = order_request.get_order_deadline_date(order_id)
            if order_support_deadline_date is None:
                support_year = int(datetime.datetime.today().year)
                support_month = int(datetime.datetime.today().month)
                support_day = int(datetime.datetime.today().day)
            else:
                support_year = int(order_support_deadline_date.year)
                support_month = int(order_support_deadline_date.month)
                if support_month == datetime.datetime.today().month:
                    support_day = int(datetime.datetime.today().day)
                else:
                    support_day = 1
                    #day = int(order_deadline_date.day)
        else:
            support_year = int(datetime.datetime.today().year)
            support_month = int(datetime.datetime.today().month)
            support_day = int(datetime.datetime.today().day)
        
        get_support_date_menu = GetDateMenuKeyboard(self.language, support_year, support_month, support_day)
        order_percent_complet_menu = GetOrderPercentCompleteMenuKeyboard(self.language, order_id)
        order_duration_menu = GetDurationMenuKeyboard(self.language)

        #------------------------------------------------------------------------------
        self.BAD_USER_ANSWER_MESSAGE = (message_object.BAD_USER_ANSWER_MESSAGE, None)

        self.START_COMMAND_VIEW = (message_object.START_MESSAGE, None)

        self.HELP_COMMAND_VIEW = (message_object.HELP_COMMAND_MESSAGE, None)

        self.CHECKING_USER_SUBSCRIPTION_STEP = (message_object.CHECKING_USER_SUBSCRIPTION_MESSAGE,
                                                checking_user_subscription_menu.checking_user_subscription_menu_keyboard)

        self.CLIENT_MAIN_MENU = (message_object.CLIENT_MAIN_MENU_MESSAGE,
                                self.client_main_menu.client_main_menu_keyboard)
        
        self.CLIENT_AND_SOLVER_MAIN_MENU = (message_object.CLIENT_AND_SOLVER_MAIN_MENU_MESSAGE,
                                            self.client_and_solver_main_menu.client_and_solver_main_menu_keyboard)
        
        self.PARTNER_MAIN_MENU = (message_object.PARTNER_MAIN_MENU_MESSAGE,
                                    partner_main_menu.partner_main_menu_keyboard)
        
        self.ADMIN_MAIN_MENU = (message_object.ADMIN_MAIN_MENU_MESSAGE,
                                admin_main_menu.admin_main_menu_keyboard)
        
        self.ACCOUNTANT_MAIN_MENU = (message_object.ACCOUNTANT_MAIN_MENU_MESSAGE,
                                        accountant_main_menu.accountant_main_menu_keyboard)
        
        self.CREATOR_MAIN_MENU = (message_object.CREATOR_MAIN_MENU_MESSAGE,
                                    creator_main_menu.creator_main_menu_keyboard)
        
        self.SETTING_UP_USER_LANGUAGE_STEP = (message_object.SETTING_UP_USER_LANGUAGE_MESSAGE,
                                                languages_kb.languages_keyboard) #пользователь задаёт язык
        
        self.SETTING_UP_USER_TIME_ZONE_STEP = (message_object.SETTING_UP_USER_TIME_ZONE_MESSAGE,
                                                time_zone_kb.time_zone_keyboard)

        self.RESETTING_UP_USER_LANGUAGE_STEP = (message_object.RESETTING_UP_USER_LANGUAGE_STEP,
                                                languages_kb.languages_keyboard)
        
        self.PARTNER_CONTROL_MENU = (message_object.PARTNER_CONTROL_MENU_MESSAGE, None)

        self.ADMIN_CONTROL_MENU = (message_object.ADMIN_CONTROL_MENU_MESSAGE, None)

        self.ACCOUNTANT_CONTROL_MENU = (message_object.ACCOUNTANT_CONTROL_MENU_MESSAGE, None)

        self.CREATOR_CONTROL_MENU = (message_object.CREATOR_CONTROL_MENU_MESSAGE, None)

        #main menu
        self.NEW_ORDER_STEP = (message_object.NEW_ORDER_MESSAGE, new_order_menu.new_order_menu_keyboard)

        self.ACTIVE_ORDERS_STEP = (message_object.ACTIVE_ORDERS_MESSAGE, None)

        self.MY_PROFILE_STEP = (message_object.MY_PROFILE_MESSAGE, my_profile_menu.my_profile_menu_keyboard)#

        self.BALANCE_STEP = (message_object.BALANCE_MESSAGE, balance_menu.balance_menu_keyboard)#

        self.SUPPORT_STEP = (message_object.SUPPORT_MESSAGE, support_kb.support_menu_keyboard)#!!!!!!!!!!!!!!!

        self.REVIEWS_STEP = (message_object.REVIEWS_MESSAGE, back_menu.back_menu_keyboard)#!!!!!!!!!!!!!!!!!!!

        self.AFFILIATE_PROGRAM_STEP = (message_object.AFFILIATE_PROGRAM_MESSAGE,
                                        affiliate_program_menu.affiliate_program_menu_keyboard)#

        self.SOLVER_MENU_STEP = (message_object.SOLVER_MENU_MESSAGE, None)

        #new order menu
        self.NEW_ORDER_BY_ADMIN_STEP = (message_object.NEW_ORDER_BY_ADMIN_MESSAGE, back_menu.back_menu_keyboard)
        self.NEW_ORDER_BY_BOT_STEP = (message_object.NEW_ORDER_BY_BOT_MESSAGE,
                                        order_importance_menu.order_importance_menu_keyboard)
        self.UNFINISHED_ORDER_STEP = (message_object.UNFINISHED_ORDER_MESSAGE, None)

        self.MAIN_STANDART_ORDER_MENU_STEP = (message_object.GET_ORDER_SETTINGS_MESSAGE, main_standart_order_menu.main_standart_menu_keyboard)
        self.MAIN_NOW_ORDER_MENU_STEP = (message_object.GET_ORDER_SETTINGS_MESSAGE, main_now_order_menu.main_now_order_menu_keyboard)
        self.MAIN_IMPORTANT_ORDER_MENU_STEP = (message_object.GET_ORDER_SETTINGS_MESSAGE, main_important_order_menu.main_important_order_menu_keyboard)
        self.MAIN_VOLUMINOUS_ORDER_MENU_STEP = (message_object.GET_ORDER_SETTINGS_MESSAGE, main_voluminous_order_menu.main_voluminous_order_menu_keyboard)

        #standart order menu
        self.GET_ORDER_SUBJECT_STEP = (message_object.GET_ORDER_SUBJECT_MESSAGE, subject_menu.subject_menu_keyboard)
        self.GET_ORDER_COMMENT_STEP = (message_object.GET_ORDER_COMMENT_MESSAGE, None)
        self.GET_ORDER_FILES_STEP = (message_object.GET_ORDER_FILES_MESSAGE, get_order_files_menu.get_order_files_menu_keyboard)
        self.GET_ORDER_DEADLINE_DATE_STEP = (message_object.GET_ORDER_DEADLINE_DATE_MESSAGE, get_date_keyboard.get_date_menu_keyboard)
        self.GET_ORDER_DEADLINE_TIME_STEP = (message_object.GET_ORDER_DEADLINE_TIME_MESSAGE, get_time_keyboard.get_time_menu_keyboard)
        self.GET_ORDER_NUMBER_OF_TASKS_STEP = (message_object.GET_ORDER_NUMBER_OF_TASKS_MESSAGE, None)
        self.GET_ORDER_DURATION_TIME_STEP = (message_object.GET_ORDER_DURATION_TIME_MESSAGE, order_duration_menu.duration_menu_keyboard)
        self.GET_UP_ORDER_SETTINGS_STEP = (message_object.GET_UP_ORDER_SETTINGS_MESSAGE, additional_order_settings_menu.additional_order_settings_menu_keyboard)
        self.SEND_ORDER_TO_SOLVERS_STEP = (message_object.SEND_ORDER_TO_SOLVERS_MESSAGE, check_order_complite_menu.check_order_complite_menu_keyboard)

        #my profile menu
        self.SET_BANKING_DETAILS_STEP = (message_object.SET_BANKING_DETAILS_MESSAGE, None)
        self.SET_CURRENCY_STEP = (message_object.SET_CURRENCY_MESSAGE, None)
        self.SET_LANGUAGE_STEP = (message_object.SET_LANGUAGE_MESSAGE, None)

        #balance_menu
        self.CASH_IN_STEP = (message_object.CASH_IN_MESSAGES, None)
        self.CASH_OUT_STEP = (message_object.CASH_OUT_MESSAGES, None)

        #support menu
        self.BECOME_A_PARTNER_STEP = (message_object.BECOME_A_PARTNER_MESSAGE, back_menu.back_menu_keyboard)
        self.BECOME_A_SOLVER_STEP = (message_object.BECOME_A_SOLVER_MESSAGE, back_menu.back_menu_keyboard)
        self.ASK_A_QUESTION_STEP = (message_object.ASK_A_QUESTION_MESSAGE, back_menu.back_menu_keyboard)
        self.FAQ_STEP = (message_object.FAQ_MESSAGE, support_faq_kb.support_faq_menu_keyboard)

        #affiliate program menu
        self.LIST_AFFILIATE_LINKS_STEP = (message_object.LIST_AFFILIATE_LINKS_MESSAGE, None)
        self.CREATE_AFFILIATE_LINK_STEP = (message_object.CREATE_AFFILIATE_LINK_MESSAGE, None)
        self.AFFILIATE_PROGRAM_STATISTICS_STEP = (message_object.AFFILIATE_PROGRAM_STATISTICS_MESSAGE, None)

        #topic views
        self.MATHS_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, maths_topics_menu.maths_menu_keyboard)
        self.PHYSICS_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, physics_topics_menu.physics_menu_keyboard)
        self.IT_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, it_topics_menu.it_menu_keyboard)
        self.ENGINEERING_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, engineering_topics_menu.engineering_menu_keyboard)
        self.ECONOMY_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, economy_topics_menu.economy_menu_keyboard)
        self.CHEMISTRY_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, chemistry_topics_menu.chemistry_menu_keyboard)
        self.LANGUAGES_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, languages_topics_menu.languages_topic_menu_keyboard)
        self.BIOLOGY_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, biology_topics_menu.biology_topic_menu_keyboard)
        self.GEOGRAPHY_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, geography_topics_menu.geography_topic_menu_keyboard)
        self.HUMANITARIAN_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, humanitarian_topics_menu.humanitarian_topic_menu_keyboard)
        self.REGISTRATION_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, registration_topics_menu.registration_topic_menu_keyboard)
        self.OTHER_TOPIC = (message_object.GET_ORDER_TOPIC_MESSAGE, None)

        #additional menu
        self.GET_ORDER_SUPPORT_DATE_STEP = (message_object.GET_ORDER_SUPPORT_DATE_MESSAGE,
                                            get_support_date_menu.get_date_menu_keyboard)

        self.GET_ORDER_SUPPORT_TIME_STEP = (message_object.GET_ORDER_SUPPORT_TIME_MESSAGE,
                                            get_time_keyboard.get_time_menu_keyboard)

        self.GET_ORDER_SUPPORT_COMMENT_STEP = (message_object.GET_ORDER_SUPPORT_COMMENT_MESSAGE, None)
        
        self.GET_ORDER_PERCENT_COMPLET_STEP = (message_object.GET_ORDER_PERCENT_COMPLET_MESSAGE,
                                                order_percent_complet_menu.get_order_percent_menu_keyboard)
        
        self.GET_ORDER_PREFERRED_BUDGET_STEP = (message_object.GET_ORDER_PREFERRED_BUDGET_MESSAGE, None)
        
        self.GET_ORDER_FORMAT_STEP = (message_object.GET_ORDER_FORMAT_MESSAGE,
                                        get_order_format_keyboard.order_format_menu_keyboard)