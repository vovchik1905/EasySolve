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


CALLBACK_DATA_INTO_ORDER_FORMAT = {ButtonCallbackData.CONTROL_FORMAT_CALLBACK_DATA: "CONTROL",
                                    ButtonCallbackData.HOMEWORK_FORMAT_CALLBACK_DATA: "HOMEWORK",
                                    ButtonCallbackData.EXAM_FORMAT_CALLBACK_DATA: "EXAM",
                                    ButtonCallbackData.LABA_FORMAT_CALLBACK_DATA: "LABA",
                                    ButtonCallbackData.COURSEWORK_FORMAT_CALLBACK_DATA: "COURSEWORK",
                                    ButtonCallbackData.DIPLOMA_FORMAT_CALLBACK_DATA: "DIPLOMA",
                                    ButtonCallbackData.OTHER_FORMAT_CALLBACK_DATA: "OTHER"}
CALLBACK_DATA_LIST = [ButtonCallbackData.CONTROL_FORMAT_CALLBACK_DATA,
                        ButtonCallbackData.HOMEWORK_FORMAT_CALLBACK_DATA,
                        ButtonCallbackData.EXAM_FORMAT_CALLBACK_DATA,
                        ButtonCallbackData.LABA_FORMAT_CALLBACK_DATA,
                        ButtonCallbackData.COURSEWORK_FORMAT_CALLBACK_DATA,
                        ButtonCallbackData.DIPLOMA_FORMAT_CALLBACK_DATA,
                        ButtonCallbackData.OTHER_FORMAT_CALLBACK_DATA,
                        ButtonCallbackData.BACK_CALLBACK_DATA]


class GetOrderFormatStep(StepModel):
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
    def update_created_order_format(tg_id: int, order_format_name: str) -> Any:
        created_order_id = GetOrderFormatStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        order_format_id = order_request.get_order_format_id(order_format_name)
        order_request.update_order_format(created_order_id, order_format_id)
        return created_order_id
    
    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = GetOrderFormatStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name
    
    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        if callback_data in CALLBACK_DATA_LIST:
            return BotStates.GET_UP_ORDER_SETTINGS_STEP
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        callback_data = data["data"]
        if callback_data in CALLBACK_DATA_INTO_ORDER_FORMAT:
            order_format = CALLBACK_DATA_INTO_ORDER_FORMAT[callback_data]
            GetOrderFormatStep.update_created_order_format(data.from_user.id, order_format)
        order_id = GetOrderFormatStep.get_created_order_id(data.from_user.id)
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
            view_object = Views("RUSSIAN", message.from_user.id)
            msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE
            await message.answer(msg, reply_markup = keyboard)
    
    @property
    def action(self):
        self.view()