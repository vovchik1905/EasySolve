from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State
from aiogram import types
from aiogram.dispatcher import FSMContext
from typing import Any

from bot_model.app.db.runtime_storage.runtime_storage import *
from bot_model.app.step_models.commands.bot_commands import BotCommand
from bot_model.app.step_models.step_model import StepModel
from bot_model.app.step_models.messages.messages import Messages
from bot_model.app.db.requests.language_requests import language_request
from bot_model.app.db.requests.currency_requests import currency_request
from bot_model.app.db.requests.payment_info_requests import payment_info_request
from bot_model.app.db.requests.telegram_requests import TelegramRequests, telegram_request
from bot_model.app.db.requests.user_requests import UserRequests, user_request
from bot_model.app.db.requests.main_requests import MainRequests, main_request
from bot_model.app.states.states import BotStates
from bot_model.app.step_models.states_views import StatesViews
from bot_model.app.step_models.views.views import Views
from settings.general.user_privileges import UserPrivileges, INT_TO_USER_PRIVILEGES
from bot_model.app.step_models.keyboards.button_headings import ButtonCallbackData
from settings.general.general_settings import GeneralSettings
from settings.general.order_state import STATE_ORDER, OrderStateEnum
from settings.general.order_importance import OrderImportanceEnum, IMPORTANCE_ORDER
from bot_model.app.db.requests.order_request import OrderRequests, order_request
from bot_model.app.step_models.check_order_complete.check_order_complete import CheckOrderComplete
from bot_model.app.step_models.messages.messages import Messages
from settings.general.order_importance import OrderImportanceEnum, IMPORTANCE_ORDER, ORDER_IMPORTANCE
from settings.general.order_format import ORDER_FORMAT, OrderFormatEnum
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings


NEW_STANDART_ORDER_CALLBACK_DATA = [ButtonCallbackData.NEW_STANDART_ORDER_IMPORTANCE_CALLBACK_DATA,
                                    ButtonCallbackData.NEW_STANDART_ORDER_SUBJECT_CALLBACK_DATA,
                                    ButtonCallbackData.NEW_STANDART_ORDER_COMMENT_CALLBACK_DATA,
                                    ButtonCallbackData.NEW_STANDART_ORDER_FILES_CALLBACK_DATA,
                                    ButtonCallbackData.NEW_STANDART_ORDER_DEADLINE_TIME_CALLBACK_DATA,
                                    ButtonCallbackData.UP_ORDER_SETTINGS_CALLBACK_DATA,
                                    ButtonCallbackData.BACK_CALLBACK_DATA]


class MainStandartOrderStep(StepModel):
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        super().__init__(bot, dp, state)
    
    @staticmethod
    def get_created_order_id(tg_id: int) -> Any:
        order_status_id = main_request.get_order_status_id_with_order_status_name(STATE_ORDER[OrderStateEnum.ORDER_CREATED])
        user_telegram = telegram_request.get_telegram_id(tg_id)
        user_id = user_request.get_user_id(user_telegram)
        created_order_id = order_request.get_or_none_status_order_id_with_user_id(user_id, order_status_id)
        if created_order_id is None:
            return None
        return created_order_id
    
    @staticmethod
    def update_created_order_status(tg_id: int, order_status_name: str) -> Any:
        created_order_id = MainStandartOrderStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        new_order_status_id = main_request.get_order_status_id_with_order_status_name(order_status_name)
        order_request.update_order_status(created_order_id, new_order_status_id)
        return created_order_id
    
    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = MainStandartOrderStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name
    
    @staticmethod
    def get_order_parameters(order_id: int) -> dict:
        parameters = order_request.get_all_fields(order_id)
        ORDER_PARAMETERS = {"id": order_id,
                            "user_id": parameters.user_id,
                            "status_id": parameters.status,
                            "format_id": parameters.format,
                            "subject": parameters.subject,
                            "topic": parameters.topic,
                            "percent_complet": parameters.percent_complet,
                            "start_date": parameters.start_date,
                            "start_time": parameters.start_time,
                            "deadline_date": parameters.deadline_date,
                            "deadline_time": parameters.deadline_time,
                            "preferred_budget": parameters.preferred_budget,
                            "comment": parameters.comment,
                            "importance": parameters.importance,
                            "number_of_tasks": parameters.number_of_tasks,
                            "duration_time": parameters.duration_time,
                            "support": parameters.support,
                            "support_date": parameters.support_date,
                            "support_time": parameters.support_time,
                            "support_comment": parameters.support_comment}
        
        order_importance = MainStandartOrderStep.get_order_importance(order_id)
        if ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.STANDARD:
            ORDER_PARAMETERS["importance"] = ButtonHeadings.NEW_STANDART_ORDER_IMPORTANCE_HEADING
        elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.NOW:
            ORDER_PARAMETERS["importance"] = ButtonHeadings.NEW_NOW_ORDER_IMPORTANCE_HEADING
        elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.IMPORTANT:
            ORDER_PARAMETERS["importance"] = ButtonHeadings.NEW_IMPORTANT_ORDER_IMPORTANCE_HEADING
        elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.VOLUMINOUS:
            ORDER_PARAMETERS["importance"] = ButtonHeadings.NEW_VOLUMINOUS_ORDER_IMPORTANCE_HEADING

        #RUSSIANORDERFORMAT
        order_format = ORDER_FORMAT[order_request.get_order_format_name(order_id)]
        return ORDER_PARAMETERS


    
    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        
        if callback_data == ButtonCallbackData.NEW_STANDART_ORDER_IMPORTANCE_CALLBACK_DATA:
            return BotStates.NEW_ORDER_BY_BOT_STEP
        
        elif callback_data == ButtonCallbackData.NEW_STANDART_ORDER_SUBJECT_CALLBACK_DATA:
            return BotStates.GET_ORDER_SUBJECT_STEP
        
        elif callback_data == ButtonCallbackData.NEW_STANDART_ORDER_COMMENT_CALLBACK_DATA:
            return BotStates.GET_ORDER_COMMENT_STEP
        
        elif callback_data == ButtonCallbackData.NEW_STANDART_ORDER_FILES_CALLBACK_DATA:
            return BotStates.GET_ORDER_FILES_STEP
        
        elif callback_data == ButtonCallbackData.NEW_STANDART_ORDER_DEADLINE_TIME_CALLBACK_DATA:
            return BotStates.GET_ORDER_DEADLINE_DATE_STEP

        elif callback_data == ButtonCallbackData.UP_ORDER_SETTINGS_CALLBACK_DATA:
            return BotStates.GET_UP_ORDER_SETTINGS_STEP

        elif callback_data == ButtonCallbackData.SEND_ORDER_TO_SOLVERS_CALLBACK_DATA:
            order_id = MainStandartOrderStep.get_created_order_id(data.from_user.id)
            order_complete_check_obj = CheckOrderComplete(order_id)
            if order_complete_check_obj.check_all_standart_order_settings():
                return BotStates.SEND_ORDER_TO_SOLVERS_STEP
            return self.state
        
        elif callback_data == ButtonCallbackData.BACK_CALLBACK_DATA:
            MainStandartOrderStep.update_created_order_status(data.from_user.id, STATE_ORDER[OrderStateEnum.ORDER_FROZEN])
            return BotStates.NEW_ORDER_BY_BOT_STEP
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        callback_data = data["data"]
        order_id = MainStandartOrderStep.get_created_order_id(data.from_user.id)
        
        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id, order_id)
        return states_views_object.STATES_VIEWS[next_state]

    
    def view(self) -> None:
        @self.dp.callback_query_handler(lambda call: call.data in NEW_STANDART_ORDER_CALLBACK_DATA, state = self.state)
        async def russian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        

        @self.dp.callback_query_handler(text = ButtonCallbackData.SEND_ORDER_TO_SOLVERS_CALLBACK_DATA, state = self.state)
        async def standart_importance_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            """"""
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            
            if next_state == BotStates.MAIN_STANDART_ORDER_MENU_STEP:
                await callback_query.answer(Messages.BAD_SEND_ORDER_MESSAGE, show_alert=True)
            else:
                order_params = MainStandartOrderStep.get_order_parameters(MainStandartOrderStep.get_created_order_id(callback_query.from_user.id))
                order_msg = f"ID: {order_params['order_id']}\n{order_params['importance']}"
                await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
                await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
                await callback_query.answer()

            await next_state.set()


        @self.dp.message_handler(state = self.state)
        async def setting_up_language_step_view(message: types.Message, state: FSMContext):
            view_object = Views("RUSSIAN", message.from_user.id)
            msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE
            await message.answer(msg, reply_markup = keyboard)
    
    @property
    def action(self):
        self.view()