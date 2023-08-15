from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from settings.views.commands.bot_commands import BotCommand
from bot_model.app.states.states import BotStates
from bot_model.app.steps.start_command.start_command import StartCommand
from bot_model.app.steps.help_command.help_command import HelpCommand
from bot_model.app.steps.checking_user_subscription_step.checking_user_subscription_step import CheckingUserSubscriptionStep
from bot_model.app.steps.setting_up_user_language_step.setting_up_user_language_step import SettingUpUserLanguageStep
from bot_model.app.steps.setting_up_user_time_zone.setting_up_user_time_zone import SettingUpUserTimeZoneStep
from bot_model.app.steps.client_main_menu_step.client_main_menu_step import ClientMainMenuStep
from bot_model.app.steps.client_and_solver_main_menu_step.client_and_solver_main_menu_step import ClientAndSolverMainMenuStep
from bot_model.app.steps.partner_main_menu_step.partner_main_menu_step import PartnerMainMenuStep
from bot_model.app.steps.admin_main_menu_step.admin_main_menu_step import AdminMainMenuStep
from bot_model.app.steps.accountant_main_menu_step.accountant_main_menu_step import AccountantMainMenuStep
from bot_model.app.steps.creator_main_menu_step.creator_main_menu_step import CreatorMainMenuStep
from bot_model.app.steps.support_step.support_step import SupportStep
from bot_model.app.steps.support_faq_step.support_faq_step import SupportFaqStep
from bot_model.app.steps.become_a_partner_step.become_a_partner_step import BecomePartnerStep
from bot_model.app.steps.become_a_solver_step.become_a_solver_step import BecomeSolverStep
from bot_model.app.steps.ask_a_question_step.ask_a_question_step import AskQuestionStep
from bot_model.app.steps.reviews_step.reviews_step import ReviewsStep
from bot_model.app.steps.balance_step.balance_step import BalanceStep
from bot_model.app.steps.my_profile_menu_step.my_profile_menu_step import MyProfileStep
from bot_model.app.steps.affiliate_program_step.affiliate_program_step import AffiliateProgramStep
from bot_model.app.steps.new_order_step.new_order_step import NewOrderStep
from bot_model.app.steps.new_order_by_admin_step.new_order_by_admin_step import NewOrderByAdminStep
from bot_model.app.steps.new_order_get_importance_step.new_order_get_importance_step import NewOrderGetImportanceStep
from bot_model.app.steps.main_standart_order_menu_step.main_standart_order_menu_step import MainStandartOrderStep
from bot_model.app.steps.get_order_subject_step.get_order_subject_step import GetOrderSubjectStep
from bot_model.app.steps.get_order_topic_step.get_order_topic_step import GetOrderTopicStep
from bot_model.app.steps.get_order_deadline_date.get_order_deadline_date_step import GetOrderDeadlineDateStep
from bot_model.app.steps.get_order_deadline_time_step.get_order_deadline_time_step import GetOrderDeadlineTimeStep
from bot_model.app.steps.get_order_comment_step.get_order_comment_step import GetOrderCommentStep
from bot_model.app.steps.get_order_file_step.get_order_file_step import GetOrderFilesStep
from bot_model.app.steps.get_order_additional_settings.additional_settings_menu_step import AdditionalOrderSettingsMenuStep
from bot_model.app.steps.get_order_additional_settings.get_order_type_setting import GetOrderFormatStep
from bot_model.app.steps.get_order_additional_settings.get_order_percent_complet_setting import GetOrderPercentCompletStep
from bot_model.app.steps.get_order_additional_settings.get_order_preferred_budget_setting import GetOrderPreferredBudgetStep
from bot_model.app.steps.get_order_additional_settings.get_order_support_date_step import GetOrderSupportDeadlineDateStep
from bot_model.app.steps.get_order_additional_settings.get_order_support_time_step import GetOrderSupportTimeStep
from bot_model.app.steps.get_order_additional_settings.get_order_support_comment_step import GetOrderSupportCommentStep
from bot_model.app.steps.main_now_order_menu_step.main_now_order_menu_step import MainNowOrderStep
from bot_model.app.steps.get_number_of_tasks_step.get_number_of_tasks_step import GetOrderNumberOfTasksStep
from bot_model.app.steps.get_order_duration_time_step.get_order_duration_time_step import GetOrderDurationTimeStep
from bot_model.app.steps.main_important_order_menu_step.main_important_order_menu_step import MainImportantOrderStep
from bot_model.app.steps.main_voluminous_order_menu_step.main_voluminous_order_menu_step import MainVoluminousOrderStep


class Handler():
    def __init__(self, bot: Bot, dp: Dispatcher) -> None:
        self.bot = bot
        self.dp = dp
    
    @property
    def start_command(self):
        start_command = StartCommand(self.bot, self.dp, BotCommand.START_COMMAND)
        start_command.action
    
    @property
    def help_command(self):
        help_command = HelpCommand(self.bot, self.dp, BotCommand.HELP_COMMAND)
        help_command.action
    
    @property
    def checking_user_subscription_step(self):
        checking_user_subscription_step = CheckingUserSubscriptionStep(self.bot, self.dp,
                                                                        BotStates.CHECKING_USER_SUBSCRIPTION_STEP)
        checking_user_subscription_step.action
    
    @property
    def setting_up_user_language_step(self):
        setting_up_user_language_step = SettingUpUserLanguageStep(self.bot, self.dp, BotStates.SETTING_UP_USER_LANGUAGE)
        setting_up_user_language_step.action
    
    @property
    def setting_up_user_time_zone_step(self):
        setting_up_user_time_zone_step = SettingUpUserTimeZoneStep(self.bot, self.dp, BotStates.SETTING_UP_USER_TIME_ZONE)
        setting_up_user_time_zone_step.action
    
    @property
    def client_main_menu_step(self):
        client_main_menu_step = ClientMainMenuStep(self.bot, self.dp,
                                                    BotStates.CLIENT_MAIN_MENU)
        client_main_menu_step.action
    
    @property
    def client_and_solver_main_menu_step(self):
        client_and_solver_main_menu_step = ClientAndSolverMainMenuStep(self.bot, self.dp,
                                                                        BotStates.CLIENT_AND_SOLVER_MAIN_MENU)
        client_and_solver_main_menu_step.action

    @property
    def partner_main_menu_step(self):
        partner_main_menu_step = PartnerMainMenuStep(self.bot, self.dp,
                                                        BotStates.PARTNER_MAIN_MENU)
        partner_main_menu_step.action
    
    @property
    def admin_main_menu_step(self):
        admin_main_menu_step = AdminMainMenuStep(self.bot, self.dp,
                                                    BotStates.ADMIN_MAIN_MENU)
        admin_main_menu_step.action
    
    @property
    def accountant_main_menu_step(self):
        accountant_main_menu_step = AccountantMainMenuStep(self.bot, self.dp,
                                                            BotStates.ACCOUNTANT_MAIN_MENU)
        accountant_main_menu_step.action
    
    @property
    def creator_main_menu_step(self):
        creator_main_menu_step = CreatorMainMenuStep(self.bot, self.dp,
                                                        BotStates.CREATOR_MAIN_MENU)
        creator_main_menu_step.action
    
    @property
    def reviews_step(self):
        reviews_step = ReviewsStep(self.bot, self.dp,
                                    BotStates.REVIEWS_STEP)
        reviews_step.action

    @property
    def support_step(self):
        support_step = SupportStep(self.bot, self.dp,
                                    BotStates.SUPPORT_STEP)
        support_step.action
    
    @property
    def support_faq_step(self):
        support_faq_step = SupportFaqStep(self.bot, self.dp,
                                            BotStates.FAQ_STEP)
        support_faq_step.action
    
    @property
    def become_a_partner_step(self):
        become_a_partner_step = BecomePartnerStep(self.bot, self.dp,
                                                    BotStates.BECOME_A_PARTNER_STEP)
        become_a_partner_step.action
    
    @property
    def become_a_solver_step(self):
        become_a_solver_step = BecomeSolverStep(self.bot, self.dp,
                                                    BotStates.BECOME_A_SOLVER_STEP)
        become_a_solver_step.action
    
    @property
    def ask_a_question_step(self):
        ask_a_question_step = AskQuestionStep(self.bot, self.dp,
                                                    BotStates.ASK_A_QUESTION_STEP)
        ask_a_question_step.action
    
    @property
    def balance_step(self):
        balance_step = BalanceStep(self.bot, self.dp,
                                    BotStates.BALANCE_STEP)
        balance_step.action
    
    @property
    def my_profile_step(self):
        my_profile_step = MyProfileStep(self.bot, self.dp,
                                        BotStates.MY_PROFILE_STEP)
        my_profile_step.action
    
    @property
    def affiliate_program_step(self):
        affiliate_program_step = AffiliateProgramStep(self.bot, self.dp,
                                                        BotStates.AFFILIATE_PROGRAM_STEP)
        affiliate_program_step.action
    
    @property
    def new_order_step(self):
        new_order_step = NewOrderStep(self.bot, self.dp,
                                        BotStates.NEW_ORDER_STEP)
        new_order_step.action
    
    @property
    def new_order_by_admin_step(self):
        new_order_by_admin_step = NewOrderByAdminStep(self.bot, self.dp,
                                                        BotStates.NEW_ORDER_BY_ADMIN_STEP)
        new_order_by_admin_step.action
    
    @property
    def new_order_get_importance_step(self):
        new_order_get_importance_step = NewOrderGetImportanceStep(self.bot, self.dp,
                                                                    BotStates.NEW_ORDER_BY_BOT_STEP)
        new_order_get_importance_step.action
    
    @property
    def main_standart_oreder_menu_step(self):
        main_standart_oreder_menu_step = MainStandartOrderStep(self.bot, self.dp,
                                                                BotStates.MAIN_STANDART_ORDER_MENU_STEP)
        main_standart_oreder_menu_step.action
    
    @property
    def get_order_subject_step(self):
        get_order_subject_step = GetOrderSubjectStep(self.bot, self.dp,
                                                        BotStates.GET_ORDER_SUBJECT_STEP)
        get_order_subject_step.action
    
    @property
    def get_order_topic_step(self):
        get_order_topic_step = GetOrderTopicStep(self.bot, self.dp,
                                                    BotStates.GET_ORDER_TOPIC_STEP)
        get_order_topic_step.action
    
    @property
    def get_order_deadline_date_step(self):
        get_order_deadline_date_step = GetOrderDeadlineDateStep(self.bot, self.dp,
                                                                    BotStates.GET_ORDER_DEADLINE_DATE_STEP)
        get_order_deadline_date_step.action

    @property
    def get_order_deadline_time_step(self):
        get_order_deadline_time_step = GetOrderDeadlineTimeStep(self.bot, self.dp,
                                                                    BotStates.GET_ORDER_DEADLINE_TIME_STEP)
        get_order_deadline_time_step.action

    @property
    def get_order_comment_step(self):
        get_order_comment_step = GetOrderCommentStep(self.bot, self.dp,
                                                        BotStates.GET_ORDER_COMMENT_STEP)
        get_order_comment_step.action

    @property
    def get_order_files_step(self):
        get_order_files_step = GetOrderFilesStep(self.bot, self.dp,
                                                    BotStates.GET_ORDER_FILES_STEP)
        get_order_files_step.action
    
    @property
    def get_additional_order_settings_menu_step(self):
        get_additional_order_settings_menu_step = AdditionalOrderSettingsMenuStep(self.bot, self.dp,
                                                                                    BotStates.GET_UP_ORDER_SETTINGS_STEP)
        get_additional_order_settings_menu_step.action

    @property
    def get_order_format_step(self):
        get_order_format_step = GetOrderFormatStep(self.bot, self.dp,
                                                    BotStates.GET_ORDER_FORMAT_STEP)
        get_order_format_step.action
    
    @property
    def get_order_percent_complet_step(self):
        get_order_percent_complet_step = GetOrderPercentCompletStep(self.bot, self.dp,
                                                                    BotStates.GET_ORDER_PERCENT_COMPLET_STEP)
        get_order_percent_complet_step.action
    
    @property
    def get_order_preferred_budget_step(self):
        get_order_preferred_budget_step = GetOrderPreferredBudgetStep(self.bot, self.dp,
                                                                        BotStates.GET_ORDER_PREFERRED_BUDGET_STEP)
        get_order_preferred_budget_step.action
    
    @property
    def get_order_support_deadline_date_step(self):
        get_order_support_deadline_date_step = GetOrderSupportDeadlineDateStep(self.bot, self.dp,
                                                                                BotStates.GET_ORDER_SUPPORT_DATE_STEP)
        get_order_support_deadline_date_step.action
    
    @property
    def get_order_support_deadline_time_step(self):
        get_order_support_deadline_time_step = GetOrderSupportTimeStep(self.bot, self.dp,
                                                                        BotStates.GET_ORDER_SUPPORT_TIME_STEP)
        get_order_support_deadline_time_step.action
    
    @property
    def get_order_support_comment_step(self):
        get_order_support_comment_step = GetOrderSupportCommentStep(self.bot, self.dp,
                                                                    BotStates.GET_ORDER_SUPPORT_COMMENT_STEP)
        get_order_support_comment_step.action
    
    @property
    def main_now_order_step(self):
        main_now_order_step = MainNowOrderStep(self.bot, self.dp,
                                                    BotStates.MAIN_NOW_ORDER_MENU_STEP)
        main_now_order_step.action
    
    @property
    def get_order_number_of_tasks_step(self):
        order_number_of_tasks_step = GetOrderNumberOfTasksStep(self.bot, self.dp,
                                                                    BotStates.GET_ORDER_NUMBER_OF_TASKS_STEP)
        order_number_of_tasks_step.action
    
    @property
    def get_order_duration_time_step(self):
        get_order_duration_time_step = GetOrderDurationTimeStep(self.bot, self.dp,
                                                                    BotStates.GET_ORDER_DURATION_TIME_STEP)
        get_order_duration_time_step.action
    
    @property
    def main_important_order_step(self):
        main_important_order_step = MainImportantOrderStep(self.bot, self.dp,
                                                            BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP)
        main_important_order_step.action
    
    @property
    def main_voluminous_order_step(self):
        main_voluminous_order_step = MainVoluminousOrderStep(self.bot, self.dp,
                                                                BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP)
        main_voluminous_order_step.action