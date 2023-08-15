from typing import Any
from bot_model.models.base_model import BazeBotModel
from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from bot_model.app.handler.bot_handler import Handler

class MainBotModel(BazeBotModel):
    def __init__(self, bot_token: str, bot_url: str, bot_name: str, bot_tg_link: str) -> None:
        super().__init__(bot_token, bot_url, bot_name, bot_tg_link)
    
    @property
    def action(self):
        EazySolveBot = Handler(self.bot, self.dp)
        EazySolveBot.start_command
        EazySolveBot.help_command
        #reg
        EazySolveBot.checking_user_subscription_step
        EazySolveBot.setting_up_user_language_step
        EazySolveBot.setting_up_user_time_zone_step
        #main menu
        EazySolveBot.client_main_menu_step
        EazySolveBot.client_and_solver_main_menu_step
        EazySolveBot.partner_main_menu_step
        EazySolveBot.admin_main_menu_step
        EazySolveBot.accountant_main_menu_step
        EazySolveBot.creator_main_menu_step
        #new order step
        EazySolveBot.new_order_step
        EazySolveBot.new_order_by_admin_step
        EazySolveBot.new_order_get_importance_step
        EazySolveBot.main_standart_oreder_menu_step
        EazySolveBot.main_now_order_step
        EazySolveBot.main_important_order_step
        EazySolveBot.main_voluminous_order_step

        EazySolveBot.get_order_subject_step
        EazySolveBot.get_order_topic_step
        EazySolveBot.get_order_deadline_date_step
        EazySolveBot.get_order_deadline_time_step
        EazySolveBot.get_order_comment_step
        EazySolveBot.get_order_files_step
        EazySolveBot.get_additional_order_settings_menu_step
        EazySolveBot.get_order_format_step
        EazySolveBot.get_order_percent_complet_step
        EazySolveBot.get_order_preferred_budget_step
        EazySolveBot.get_order_support_deadline_date_step
        EazySolveBot.get_order_support_deadline_time_step
        EazySolveBot.get_order_support_comment_step
        EazySolveBot.get_order_number_of_tasks_step
        EazySolveBot.get_order_duration_time_step
        #my profile step
        EazySolveBot.my_profile_step
        #balance step
        EazySolveBot.balance_step
        #reviews menu
        EazySolveBot.reviews_step
        #support menu
        EazySolveBot.support_step
        EazySolveBot.support_faq_step
        EazySolveBot.become_a_partner_step
        EazySolveBot.become_a_solver_step
        EazySolveBot.ask_a_question_step
        #affiliate program menu
        EazySolveBot.affiliate_program_step