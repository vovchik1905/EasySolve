from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State
from aiogram import types
from aiogram.dispatcher import FSMContext
import datetime
from typing import Any

from bot_model.app.db.runtime_storage.runtime_storage import *
from bot_model.app.step_models.commands.bot_commands import BotCommand
from bot_model.app.step_models.step_model import StepModel
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
from settings.general.order_importance import OrderImportanceEnum, IMPORTANCE_ORDER, ORDER_IMPORTANCE
from bot_model.app.db.requests.order_request import OrderRequests, order_request
from bot_model.app.step_models.messages.messages import Messages
from bot_model.app.step_models.keyboards.order_keyboards.deadline_time_keyboards.get_data_keyboard import GetDateMenuKeyboard
from bot_model.app.step_models.keyboards.order_keyboards.deadline_time_keyboards.get_time_keyboard import GetTimeMenuKeyboard


ORDER_DURATION_CALLBACK_DATA = [ButtonCallbackData.ORDER_1DURATION_CALLBACK_DATA,
                                ButtonCallbackData.ORDER_2DURATION_CALLBACK_DATA,
                                ButtonCallbackData.ORDER_3DURATION_CALLBACK_DATA,
                                ButtonCallbackData.ORDER_4DURATION_CALLBACK_DATA,
                                ButtonCallbackData.ORDER_5DURATION_CALLBACK_DATA,
                                ButtonCallbackData.ORDER_6DURATION_CALLBACK_DATA,
                                ButtonCallbackData.ORDER_7DURATION_CALLBACK_DATA,
                                ButtonCallbackData.ORDER_8DURATION_CALLBACK_DATA]


class GetOrderDurationTimeStep(StepModel):
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
    def update_created_order_duration_time(tg_id: int, order_deadline_time: tuple) -> Any:
        created_order_id = GetOrderDurationTimeStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        #print(order_deadline_time)
        if len(order_deadline_time) == 2:
            deadline_time = (order_deadline_time[0], order_deadline_time[1], 59)
            order_request.update_order_duration_time(created_order_id, deadline_time)
        else:
            order_request.update_order_duration_time(created_order_id, order_deadline_time)
        return created_order_id
    
    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = GetOrderDurationTimeStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name
    
    @staticmethod
    def check_order_time(order_time: str) -> bool:
        try:
            datetime.datetime.strptime(order_time, '%H:%M')
        except ValueError:
            return False
        return len(order_time) == 5
    
    @staticmethod
    def get_hour_and_minute(order_id: int) -> tuple:
            get_order_deadline_time = order_request.get_order_deadline_time(order_id)
            if get_order_deadline_time is None:
                hour = datetime.datetime.today().hour
                minute = datetime.datetime.today().minute
                minute = datetime.datetime.today().second
            else:
                hour = get_order_deadline_time.hour
                minute = get_order_deadline_time.minute
            return (hour, minute)

    async def logic(self, data: Any) -> State:
        """"""
        callback_data = data["data"]
        if callback_data in ORDER_DURATION_CALLBACK_DATA:
            order_importance = GetOrderDurationTimeStep.get_order_importance(data.from_user.id)
            if ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.STANDARD:
                return BotStates.MAIN_STANDART_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.NOW:
                return BotStates.MAIN_NOW_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.IMPORTANT:
                return BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.VOLUMINOUS:
                return BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        callback_data = data["data"]
        order_id = GetOrderDurationTimeStep.get_created_order_id(data.from_user.id)
        if callback_data in ORDER_DURATION_CALLBACK_DATA:
            if callback_data == ButtonCallbackData.ORDER_1DURATION_CALLBACK_DATA:
                order_duration_time = (0,30,59)
            elif callback_data == ButtonCallbackData.ORDER_2DURATION_CALLBACK_DATA:
                order_duration_time = (0,45,59)
            elif callback_data == ButtonCallbackData.ORDER_3DURATION_CALLBACK_DATA:
                order_duration_time = (1,0,59)
            elif callback_data == ButtonCallbackData.ORDER_4DURATION_CALLBACK_DATA:
                order_duration_time = (1,30,59)
            elif callback_data == ButtonCallbackData.ORDER_5DURATION_CALLBACK_DATA:
                order_duration_time = (2,0,59)
            elif callback_data == ButtonCallbackData.ORDER_6DURATION_CALLBACK_DATA:
                order_duration_time = (3,0,59)
            elif callback_data == ButtonCallbackData.ORDER_7DURATION_CALLBACK_DATA:
                order_duration_time = (4,30,59)
            elif callback_data == ButtonCallbackData.ORDER_8DURATION_CALLBACK_DATA:
                order_duration_time = (6,0,59)
            #print(order_duration_time)
            GetOrderDurationTimeStep.update_created_order_duration_time(data.from_user.id, order_duration_time)

        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id, order_id)
        return states_views_object.STATES_VIEWS[next_state]

    
    def view(self) -> None:
        @self.dp.callback_query_handler(lambda call: call.data in ORDER_DURATION_CALLBACK_DATA, state = self.state)
        async def russian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()


        @self.dp.message_handler(state = self.state)
        async def setting_up_language_step_view(message: types.Message, state: FSMContext):
            if GetOrderDurationTimeStep.check_order_time(message.text):
                order_deadline_time = tuple(map(int, list(message.text.split(":"))))
                GetOrderDurationTimeStep.update_created_order_duration_time(message.from_user.id, order_deadline_time)
                order_importance = GetOrderDurationTimeStep.get_order_importance(message.from_user.id)
                if ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.STANDARD:
                    next_state = BotStates.MAIN_STANDART_ORDER_MENU_STEP
                elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.NOW:
                    next_state = BotStates.MAIN_NOW_ORDER_MENU_STEP
                elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.IMPORTANT:
                    next_state = BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP
                elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.VOLUMINOUS:
                    next_state = BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP
                order_id = GetOrderDurationTimeStep.get_created_order_id(message.from_user.id)
                language_name = main_request.get_language_with_tg_id(message.from_user.id)
                states_views_object = StatesViews(language_name, message.from_user.id, order_id)
                output_data = states_views_object.STATES_VIEWS[next_state]
                msg, keyboard = output_data
                await message.answer(msg, reply_markup = keyboard)
                await next_state.set()
            else:
                view_object = Views("RUSSIAN", message.from_user.id)
                msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE
                await message.answer(msg, reply_markup = keyboard)
    
    @property
    def action(self):
        self.view()