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
from settings.general.order_importance import OrderImportanceEnum, IMPORTANCE_ORDER, ORDER_IMPORTANCE
from bot_model.app.db.requests.order_request import OrderRequests, order_request
from settings.general.order_topic import ORDER_TOPIC
from bot_model.app.step_models.messages.messages import Messages
from bot_model.app.step_models.views.views import Views


CALLBACK_DATA_INTO_ORDER_PERCENT_COMPLET = {ButtonCallbackData.TEN_PERCENT_CALLBACK_DATA: 10,
                                            ButtonCallbackData.TWENTY_PERCENT_CALLBACK_DATA: 20,
                                            ButtonCallbackData.THIRTY_PERCENT_CALLBACK_DATA: 30,
                                            ButtonCallbackData.FORTY_PERCENT_CALLBACK_DATA: 40,
                                            ButtonCallbackData.FIFTY_PERCENT_CALLBACK_DATA: 50,
                                            ButtonCallbackData.SIXTY_PERCENT_CALLBACK_DATA: 60,
                                            ButtonCallbackData.SEVENTY_PERCENT_CALLBACK_DATA: 70,
                                            ButtonCallbackData.EIGHTY_PERCENT_CALLBACK_DATA: 80,
                                            ButtonCallbackData.NINETY_PERCENT_CALLBACK_DATA: 90,
                                            ButtonCallbackData.HUNDRED_PERCENT_CALLBACK_DATA: 100}
CALLBACK_DATA_LIST = [ButtonCallbackData.TEN_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.TWENTY_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.THIRTY_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.FORTY_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.FIFTY_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.SIXTY_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.SEVENTY_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.EIGHTY_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.NINETY_PERCENT_CALLBACK_DATA,
                        ButtonCallbackData.HUNDRED_PERCENT_CALLBACK_DATA]


class GetOrderPercentCompletStep(StepModel):
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
    def update_created_order_percent_complet(tg_id: int, order_percent_complet: int) -> Any:
        created_order_id = GetOrderPercentCompletStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        order_request.update_order_percent_complet(created_order_id, order_percent_complet)
        return created_order_id
    
    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = GetOrderPercentCompletStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name
    
    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        if callback_data in CALLBACK_DATA_LIST:
            return BotStates.GET_UP_ORDER_SETTINGS_STEP
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        callback_data = data["data"]
        if callback_data in CALLBACK_DATA_INTO_ORDER_PERCENT_COMPLET:
            order_percent_complet = CALLBACK_DATA_INTO_ORDER_PERCENT_COMPLET[callback_data]
            GetOrderPercentCompletStep.update_created_order_percent_complet(data.from_user.id, order_percent_complet)
        order_id = GetOrderPercentCompletStep.get_created_order_id(data.from_user.id)
        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id, order_id)
        return states_views_object.STATES_VIEWS[next_state]

    
    def view(self) -> None:
        @self.dp.callback_query_handler(lambda call: call.data in CALLBACK_DATA_LIST, state = self.state)
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
            next_state = self.state
            view_object = Views("RUSSIAN", message.from_user.id)
            msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE

            if message.text.isdigit():
                order_percent_complet = int(message.text)
                if order_percent_complet >= 0 and order_percent_complet <= 100:
                    GetOrderPercentCompletStep.update_created_order_percent_complet(message.from_user.id,
                                                                                    order_percent_complet)
                    next_state = BotStates.GET_UP_ORDER_SETTINGS_STEP
                    order_id = GetOrderPercentCompletStep.get_created_order_id(message.from_user.id)
                    language_name = main_request.get_language_with_tg_id(message.from_user.id)
                    states_views_object = StatesViews(language_name, message.from_user.id, order_id)
                    msg, keyboard = states_views_object.STATES_VIEWS[next_state]
            
            await message.answer(msg, reply_markup = keyboard)
            await next_state.set()

        #@self.dp.message_handler(state = self.state)
        #async def setting_up_language_step_view(message: types.Message, state: FSMContext):
        #    view_object = Views("RUSSIAN", message.from_user.id)
        #    msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE
        #    await message.answer(msg, reply_markup = keyboard)
    
    @property
    def action(self):
        self.view()