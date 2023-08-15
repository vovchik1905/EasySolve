from bot_model.app.step_models.commands.bot_commands import BotCommand
from bot_model.app.states.states import *
from bot_model.app.step_models.views.views import Views


class StatesViews:
    def __init__(self, language: str, user_id: int, order_id: int = None) -> None:
        self.language = language
        self.user_id = user_id
        self.views_object = Views(self.language, self.user_id, order_id)
        self.STATES_VIEWS = {BotStates.CHECKING_USER_SUBSCRIPTION_STEP: self.views_object.CHECKING_USER_SUBSCRIPTION_STEP,
                            BotStates.CLIENT_MAIN_MENU: self.views_object.CLIENT_MAIN_MENU,
                            BotStates.NEW_ORDER_STEP: self.views_object.NEW_ORDER_STEP,
                            BotStates.ACTIVE_ORDERS_STEP: self.views_object.ACTIVE_ORDERS_STEP,
                            BotStates.MY_PROFILE_STEP: self.views_object.MY_PROFILE_STEP,
                            BotStates.BALANCE_STEP: self.views_object.BALANCE_STEP,
                            BotStates.SUPPORT_STEP: self.views_object.SUPPORT_STEP,
                            BotStates.REVIEWS_STEP: self.views_object.REVIEWS_STEP,
                            BotStates.AFFILIATE_PROGRAM_STEP: self.views_object.AFFILIATE_PROGRAM_STEP,
                            BotStates.SOLVER_MENU_STEP: self.views_object.SOLVER_MENU_STEP, #mm
                            BotStates.CLIENT_AND_SOLVER_MAIN_MENU: self.views_object.CLIENT_AND_SOLVER_MAIN_MENU,
                            BotStates.PARTNER_MAIN_MENU: self.views_object.PARTNER_MAIN_MENU,
                            BotStates.ADMIN_MAIN_MENU: self.views_object.ADMIN_MAIN_MENU,
                            BotStates.ACCOUNTANT_MAIN_MENU: self.views_object.ACCOUNTANT_MAIN_MENU,
                            BotStates.CREATOR_MAIN_MENU: self.views_object.CREATOR_MAIN_MENU,
                            BotStates.SETTING_UP_USER_LANGUAGE: self.views_object.SETTING_UP_USER_LANGUAGE_STEP,
                            BotStates.SETTING_UP_USER_TIME_ZONE: self.views_object.SETTING_UP_USER_TIME_ZONE_STEP,
                            BotStates.PARTNER_CONTROL_MENU: self.views_object.PARTNER_CONTROL_MENU,
                            BotStates.ADMIN_CONTROL_MENU: self.views_object.ADMIN_CONTROL_MENU,
                            BotStates.ACCOUNTANT_CONTROL_MENU: self.views_object.ACCOUNTANT_CONTROL_MENU,
                            BotStates.CREATOR_CONTROL_MENU: self.views_object.CREATOR_CONTROL_MENU,
                            BotStates.BECOME_A_PARTNER_STEP: self.views_object.BECOME_A_PARTNER_STEP,
                            BotStates.BECOME_A_SOLVER_STEP: self.views_object.BECOME_A_SOLVER_STEP,
                            BotStates.ASK_A_QUESTION_STEP: self.views_object.ASK_A_QUESTION_STEP,
                            BotStates.FAQ_STEP: self.views_object.FAQ_STEP,
                            BotStates.CASH_IN_STEP: self.views_object.CASH_IN_STEP,
                            BotStates.CASH_OUT_STEP: self.views_object.CASH_OUT_STEP,
                            BotStates.SET_BANKING_DETAILS_STEP: self.views_object.SET_BANKING_DETAILS_STEP,
                            BotStates.SET_CURRENCY_STEP: self.views_object.SET_CURRENCY_STEP,
                            BotStates.SET_LANGUAGE_STEP: self.views_object.SET_LANGUAGE_STEP,
                            BotStates.LIST_AFFILIATE_LINKS_STEP: self.views_object.LIST_AFFILIATE_LINKS_STEP,
                            BotStates.CREATE_AFFILIATE_LINK_STEP: self.views_object.CREATE_AFFILIATE_LINK_STEP,
                            BotStates.AFFILIATE_PROGRAM_STATISTICS_STEP: self.views_object.AFFILIATE_PROGRAM_STATISTICS_STEP,
                            BotStates.NEW_ORDER_BY_ADMIN_STEP: self.views_object.NEW_ORDER_BY_ADMIN_STEP,
                            BotStates.NEW_ORDER_BY_BOT_STEP: self.views_object.NEW_ORDER_BY_BOT_STEP,
                            BotStates.UNFINISHED_ORDER_STEP: self.views_object.UNFINISHED_ORDER_STEP,
                            BotStates.MAIN_STANDART_ORDER_MENU_STEP: self.views_object.MAIN_STANDART_ORDER_MENU_STEP,
                            BotStates.MAIN_NOW_ORDER_MENU_STEP: self.views_object.MAIN_NOW_ORDER_MENU_STEP,
                            BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP: self.views_object.MAIN_IMPORTANT_ORDER_MENU_STEP,
                            BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP: self.views_object.MAIN_VOLUMINOUS_ORDER_MENU_STEP,
                            BotStates.GET_ORDER_SUBJECT_STEP: self.views_object.GET_ORDER_SUBJECT_STEP,
                            BotStates.GET_ORDER_COMMENT_STEP: self.views_object.GET_ORDER_COMMENT_STEP,
                            BotStates.GET_ORDER_FILES_STEP: self.views_object.GET_ORDER_FILES_STEP,
                            BotStates.GET_ORDER_DEADLINE_DATE_STEP: self.views_object.GET_ORDER_DEADLINE_DATE_STEP,
                            BotStates.GET_ORDER_DEADLINE_TIME_STEP: self.views_object.GET_ORDER_DEADLINE_TIME_STEP,
                            BotStates.GET_UP_ORDER_SETTINGS_STEP: self.views_object.GET_UP_ORDER_SETTINGS_STEP,
                            BotStates.SEND_ORDER_TO_SOLVERS_STEP: self.views_object.SEND_ORDER_TO_SOLVERS_STEP,
                            BotStates.GET_ORDER_SUPPORT_DATE_STEP: self.views_object.GET_ORDER_SUPPORT_DATE_STEP,
                            BotStates.GET_ORDER_PERCENT_COMPLET_STEP: self.views_object.GET_ORDER_PERCENT_COMPLET_STEP,
                            BotStates.GET_ORDER_PREFERRED_BUDGET_STEP: self.views_object.GET_ORDER_PREFERRED_BUDGET_STEP,
                            BotStates.GET_ORDER_FORMAT_STEP: self.views_object.GET_ORDER_FORMAT_STEP,
                            BotStates.GET_ORDER_SUPPORT_TIME_STEP: self.views_object.GET_ORDER_SUPPORT_TIME_STEP,
                            BotStates.GET_ORDER_SUPPORT_COMMENT_STEP: self.views_object.GET_ORDER_SUPPORT_COMMENT_STEP,
                            BotStates.GET_ORDER_NUMBER_OF_TASKS_STEP: self.views_object.GET_ORDER_NUMBER_OF_TASKS_STEP,
                            BotStates.GET_ORDER_DURATION_TIME_STEP: self.views_object.GET_ORDER_DURATION_TIME_STEP}

