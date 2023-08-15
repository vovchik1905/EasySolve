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
from settings.general.order_subject import ORDER_SUBJECT
from bot_model.app.step_models.messages.messages import Messages
from bot_model.app.step_models.views.views import Views
from settings.general.order_importance import OrderImportanceEnum, IMPORTANCE_ORDER, ORDER_IMPORTANCE


ORDER_IMPORTANCE_STATES = [BotStates.GET_UP_ORDER_SETTINGS_STEP]


class GetOrderSupportCommentStep(StepModel):
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        super().__init__(bot, dp, state)
    
    @staticmethod
    def check_order_support_comment(order_comment: str) -> bool:
        return True

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
    def update_created_order_support_comment(tg_id: int, order_support_comment: str) -> Any:
        created_order_id = GetOrderSupportCommentStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        order_request.update_order_support_comment(created_order_id, order_support_comment)
        return created_order_id
    
    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = GetOrderSupportCommentStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name

    async def logic(self, data: Any) -> State:
        order_support_comment = data.text
        if GetOrderSupportCommentStep.check_order_support_comment(order_support_comment):
            return BotStates.GET_UP_ORDER_SETTINGS_STEP
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        order_comment = data.text
        order_id = GetOrderSupportCommentStep.get_created_order_id(data.from_user.id)
        if next_state in ORDER_IMPORTANCE_STATES:
            GetOrderSupportCommentStep.update_created_order_support_comment(data.from_user.id, order_comment)
            order_request.update_order_support(order_id, True)
        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id, order_id)
        return states_views_object.STATES_VIEWS[next_state]

    def view(self) -> None:
        @self.dp.message_handler(state = self.state)
        async def setting_up_language_step_view(message: types.Message, state: FSMContext):
            next_state = await self.logic(message)
            output_data = await self.db(next_state, message)
            msg, keyboard = output_data
            if next_state in ORDER_IMPORTANCE_STATES:
                await self.bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
                await self.bot.send_message(message.from_user.id, msg, reply_markup = keyboard)
            else:
                view_object = Views("RUSSIAN", message.from_user.id)
                msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE
                await message.answer(msg, reply_markup = keyboard)
            await next_state.set()

    @property
    def action(self):
        self.view()