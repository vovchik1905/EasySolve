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


ORDER_SUBJECT_CALLBACK_DATA = [ButtonCallbackData.MATHS_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.PHYSICS_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.IT_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.ENGINEERING_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.ECONOMY_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.CHEMISTRY_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.LANGUAGES_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.BIOLOGY_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.GEOGRAPHY_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.HUMANITARIAN_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.REGISTRATION_SUBJECT_CALLBACK_DATA,
                                ButtonCallbackData.OTHER_SUBJECT_CALLBACK_DATA]

ORDER_SUBJECTS_NAMES = [sbj_name for sbj_name in ORDER_SUBJECT]

#CALLBACK_DATA_INTO_SBJ_NAME = {ORDER_SUBJECT_CALLBACK_DATA[i]: ORDER_SUBJECTS_NAMES[i+1] for i in range(len(ORDER_SUBJECT_CALLBACK_DATA))}
CALLBACK_DATA_INTO_SBJ_NAME = {ORDER_SUBJECT_CALLBACK_DATA[i]: ORDER_SUBJECTS_NAMES[i+1] for i in range(len(ORDER_SUBJECT_CALLBACK_DATA))}

#CALLBACK_DATA_INTO_STATE = {ButtonCallbackData.MATHS_SUBJECT_CALLBACK_DATA: "MATHS_TOPIC"}


class GetOrderSubjectStep(StepModel):
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
    def update_created_order_subject(tg_id: int, order_subject_name: str) -> Any:
        created_order_id = GetOrderSubjectStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        order_subject_id = order_request.get_order_subject_id(order_subject_name)
        order_request.update_order_subject(created_order_id, order_subject_id)
        return created_order_id
    
    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = GetOrderSubjectStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name
    
    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        if callback_data == ButtonCallbackData.OTHER_SUBJECT_CALLBACK_DATA:
            order_importance = GetOrderSubjectStep.get_order_importance(data.from_user.id)
            if ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.STANDARD:
                return BotStates.MAIN_STANDART_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.NOW:
                return BotStates.MAIN_NOW_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.IMPORTANT:
                return BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.VOLUMINOUS:
                return BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP
        if callback_data in ORDER_SUBJECT_CALLBACK_DATA:
            return BotStates.GET_ORDER_TOPIC_STEP
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        callback_data = data["data"]
        order_subject = CALLBACK_DATA_INTO_SBJ_NAME[callback_data]
        GetOrderSubjectStep.update_created_order_subject(data.from_user.id, order_subject)

        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        order_id = GetOrderSubjectStep.get_created_order_id(data.from_user.id)
        views_object = Views(language_name, data.from_user.id)
        if callback_data == ButtonCallbackData.MATHS_SUBJECT_CALLBACK_DATA:
            return views_object.MATHS_TOPIC
        elif callback_data == ButtonCallbackData.PHYSICS_SUBJECT_CALLBACK_DATA:
            return views_object.PHYSICS_TOPIC
        elif callback_data == ButtonCallbackData.IT_SUBJECT_CALLBACK_DATA:
            return views_object.IT_TOPIC
        elif callback_data == ButtonCallbackData.ENGINEERING_SUBJECT_CALLBACK_DATA:
            return views_object.ENGINEERING_TOPIC
        elif callback_data == ButtonCallbackData.ECONOMY_SUBJECT_CALLBACK_DATA:
            return views_object.ECONOMY_TOPIC
        elif callback_data == ButtonCallbackData.CHEMISTRY_SUBJECT_CALLBACK_DATA:
            return views_object.CHEMISTRY_TOPIC
        elif callback_data == ButtonCallbackData.LANGUAGES_SUBJECT_CALLBACK_DATA:
            return views_object.LANGUAGES_TOPIC
        elif callback_data == ButtonCallbackData.BIOLOGY_SUBJECT_CALLBACK_DATA:
            return views_object.BIOLOGY_TOPIC
        elif callback_data == ButtonCallbackData.GEOGRAPHY_SUBJECT_CALLBACK_DATA:
            return views_object.GEOGRAPHY_TOPIC
        elif callback_data == ButtonCallbackData.HUMANITARIAN_SUBJECT_CALLBACK_DATA:
            return views_object.HUMANITARIAN_TOPIC
        elif callback_data == ButtonCallbackData.REGISTRATION_SUBJECT_CALLBACK_DATA:
            return views_object.REGISTRATION_TOPIC
        #elif callback_data == ButtonCallbackData.OTHER_SUBJECT_CALLBACK_DATA:
        #    
        #    return views_object.OTHER_TOPIC
        
        states_views_object = StatesViews(language_name, data.from_user.id, order_id)
        return states_views_object.STATES_VIEWS[next_state]

    
    def view(self) -> None:
        @self.dp.callback_query_handler(lambda call: call.data in ORDER_SUBJECT_CALLBACK_DATA, state = self.state)
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