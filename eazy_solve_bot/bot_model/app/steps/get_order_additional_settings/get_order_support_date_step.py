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


ORDER_DEADLINE_DATE_CALLBACK_DATA = [f"{ButtonCallbackData.DAY_CALLBACK_DATA}_{day_num}" for day_num in range(1,32)]
NEXT_LAST_MONTH_DATE_CALLBACK_DATA = [ButtonCallbackData.LAST_MONTH_CALLBACK_DATA,
                                        ButtonCallbackData.NEXT_MONTH_CALLBACK_DATA]


class GetOrderSupportDeadlineDateStep(StepModel):
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
    def update_created_order_support_deadline_date(tg_id: int, order_deadline_date: tuple) -> Any:
        created_order_id = GetOrderSupportDeadlineDateStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        order_request.update_order_support_date(created_order_id, order_deadline_date)
        return created_order_id
    
    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = GetOrderSupportDeadlineDateStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name
    
    @staticmethod
    def check_order_date(order_date: str) -> bool:
            def validate(date_text: str) -> bool:
                try:
                   datetime.datetime.strptime(date_text, '%Y.%m.%d')
                   return True
                except ValueError:
                   return False
            
            if validate(order_date) is False:
                return False
            
            order_year, order_month, order_day = list(map(int, list(order_date.split("."))))
            order_date_obj = datetime.datetime(order_year, order_month, order_day)
            return order_date_obj >= datetime.datetime.today()
    
    @staticmethod
    def get_year_and_month(order_id: int) -> tuple:
            get_order_deadline_date = order_request.get_order_support_date(order_id)
            if get_order_deadline_date is None:
                year = datetime.datetime.today().year
                month = datetime.datetime.today().month
            else:
                year = get_order_deadline_date.year
                month = get_order_deadline_date.month
            return (year, month)

    async def logic(self, data: Any) -> State:
        """"""
        callback_data = data["data"]
        if callback_data in ORDER_DEADLINE_DATE_CALLBACK_DATA:
            return BotStates.GET_ORDER_SUPPORT_TIME_STEP
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        callback_data = data["data"]
        order_id = GetOrderSupportDeadlineDateStep.get_created_order_id(data.from_user.id)
        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        year, month = GetOrderSupportDeadlineDateStep.get_year_and_month(order_id)
        today_date = 1
        if next_state == self.state:
            if callback_data == ButtonCallbackData.LAST_MONTH_CALLBACK_DATA:
                if month == 1:
                    year -= 1
                    month = 12
                else:
                    month -= 1
                
                if month == datetime.datetime.today().month:
                    day = datetime.datetime.today().day
                else:
                    day = 1
                
                last_month_order_deadline_date = (year, month, day)
                order_date_obj = datetime.datetime(year, month, day)
                
                if order_date_obj >= datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, 1):
                    GetOrderSupportDeadlineDateStep.update_created_order_support_deadline_date(data.from_user.id,
                                                                                last_month_order_deadline_date)
                    date_keyboard = GetDateMenuKeyboard(language_name, year, month, day)
                    date_message = Messages(language_name).GET_ORDER_SUPPORT_DATE_MESSAGE
                    last_month_view = (date_message, date_keyboard.get_date_menu_keyboard)
                    return last_month_view
            
            elif callback_data == ButtonCallbackData.NEXT_MONTH_CALLBACK_DATA:
                if month == 12:
                    year += 1
                    month = 1
                else:
                    month += 1
                
                if month == datetime.datetime.today().month:
                    day = datetime.datetime.today().day
                else:
                    day = 1
                
                next_month_order_deadline_date = (year, month, day)
                order_date_obj = datetime.datetime(year, month, day)
                
                if order_date_obj >= datetime.datetime.today():
                    GetOrderSupportDeadlineDateStep.update_created_order_support_deadline_date(data.from_user.id, next_month_order_deadline_date)
                
                date_keyboard = GetDateMenuKeyboard(language_name, year, month, day)
                date_message = Messages(language_name).GET_ORDER_SUPPORT_DATE_MESSAGE
                next_month_view = (date_message, date_keyboard.get_date_menu_keyboard)
                return next_month_view
        else:
            day = int(list(str(list(callback_data.split(ButtonCallbackData.DAY_CALLBACK_DATA))[1]).split("_"))[1])
            order_deadline_date = (year, month, day)
            order_date_obj = datetime.datetime(year, month, day)
            if order_date_obj >= datetime.datetime(datetime.datetime.today().year,
                                                    datetime.datetime.today().month,
                                                    datetime.datetime.today().day):
                GetOrderSupportDeadlineDateStep.update_created_order_support_deadline_date(data.from_user.id, order_deadline_date)
        states_views_object = StatesViews(language_name, data.from_user.id, order_id)
        return states_views_object.STATES_VIEWS[next_state]

    
    def view(self) -> None:
        @self.dp.callback_query_handler(lambda call: (call.data in ORDER_DEADLINE_DATE_CALLBACK_DATA) or (call.data in NEXT_LAST_MONTH_DATE_CALLBACK_DATA), state = self.state)
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
            if GetOrderSupportDeadlineDateStep.check_order_date(message.text):
                order_deadline_date = tuple(map(int, list(message.text.split("."))))
                GetOrderSupportDeadlineDateStep.update_created_order_support_deadline_date(message.from_user.id, order_deadline_date)
                next_state = BotStates.GET_ORDER_SUPPORT_TIME_STEP
                language_name = main_request.get_language_with_tg_id(message.from_user.id)
                view_object = Views(language_name, message.from_user.id)    
                msg, keyboard = view_object.GET_ORDER_SUPPORT_TIME_STEP#!!!!!!!!!!!!!!!!!!!!
                await message.answer(msg, reply_markup = keyboard)
                await next_state.set()
            else:
                view_object = Views("RUSSIAN", message.from_user.id)
                msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE
                await message.answer(msg, reply_markup = keyboard)
    
    @property
    def action(self):
        self.view()