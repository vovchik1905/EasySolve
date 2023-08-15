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
from bot_model.app.db.requests.telegram_requests import TelegramRequests, telegram_request
from bot_model.app.db.requests.user_requests import UserRequests, user_request
from bot_model.app.db.requests.main_requests import MainRequests, main_request
from bot_model.app.db.requests.order_request import OrderRequests, order_request
from bot_model.app.states.states import BotStates
from bot_model.app.step_models.states_views import StatesViews
from settings.general.user_privileges import UserPrivileges, INT_TO_USER_PRIVILEGES
from bot_model.app.step_models.keyboards.button_headings import ButtonCallbackData
from bot_model.app.step_models.views.views import Views
from settings.general.order_state import STATE_ORDER, OrderStateEnum
from settings.general.order_importance import OrderImportanceEnum, IMPORTANCE_ORDER, ORDER_IMPORTANCE


CALLBACK_INTO_ORDER_FORMAT = {ButtonCallbackData.STANDART_IMPORTANCE_CALLBACK_DATA: OrderImportanceEnum.STANDARD,
                                ButtonCallbackData.NOW_IMPORTANCE_CALLBACK_DATA: OrderImportanceEnum.NOW,
                                ButtonCallbackData.IMPORTANT_IMPORTANCE_CALLBACK_DATA: OrderImportanceEnum.IMPORTANT,
                                ButtonCallbackData.VOLUMINOUS_IMPORTANCE_CALLBACK_DATA: OrderImportanceEnum.VOLUMINOUS}


class NewOrderGetImportanceStep(StepModel):
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        super().__init__(bot, dp, state)
    
    @staticmethod
    def get_created_order_id(tg_id: int):
        order_status_id = main_request.get_order_status_id_with_order_status_name(STATE_ORDER[OrderStateEnum.ORDER_CREATED])
        user_telegram = telegram_request.get_telegram_id(tg_id)
        user_id = user_request.get_user_id(user_telegram)
        created_order_id = order_request.get_or_none_status_order_id_with_user_id(user_id, order_status_id)
        return created_order_id


    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        created_order_id = NewOrderGetImportanceStep.get_created_order_id(data.from_user.id)
        if callback_data == ButtonCallbackData.BACK_CALLBACK_DATA:
            return BotStates.NEW_ORDER_STEP
        elif created_order_id is not None:
            order_importance = order_request.get_order_importance_name_with_order_id(created_order_id)
            if ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.STANDARD:
                return BotStates.MAIN_STANDART_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.NOW:
                return BotStates.MAIN_NOW_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.IMPORTANT:
                return BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.VOLUMINOUS:
                return BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP

        else:
            if callback_data == ButtonCallbackData.STANDART_IMPORTANCE_CALLBACK_DATA:
                return BotStates.MAIN_STANDART_ORDER_MENU_STEP
            elif callback_data == ButtonCallbackData.NOW_IMPORTANCE_CALLBACK_DATA:
                return BotStates.MAIN_NOW_ORDER_MENU_STEP
            elif callback_data == ButtonCallbackData.IMPORTANT_IMPORTANCE_CALLBACK_DATA:
                return BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP
            elif callback_data == ButtonCallbackData.VOLUMINOUS_IMPORTANCE_CALLBACK_DATA:
                return BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP
        
        return self.state

    async def db(self, next_state: State, data: Any) -> Any:
        """"""
        callback_data = data["data"]
        FORMAT_STATES = [BotStates.MAIN_STANDART_ORDER_MENU_STEP,
                        BotStates.MAIN_NOW_ORDER_MENU_STEP,
                        BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP,
                        BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP]

        def create_order(tg_id: int, order_importance_name: str):
            RuntimeStorageTelegram.tg_id = tg_id
            RuntimeStorageUser.telegram = telegram_request.get_telegram_id(RuntimeStorageTelegram.tg_id)
            RuntimeStorageUser.id = user_request.get_user_id(RuntimeStorageUser.telegram)
            RuntimeStorageOrder.importance = order_request.get_order_importance_id(order_importance_name)
            order_request.create_order(RuntimeStorageUser.id,
                                        RuntimeStorageOrder.importance)

        if callback_data != ButtonCallbackData.BACK_CALLBACK_DATA:
            if next_state in FORMAT_STATES:
                important_name = IMPORTANCE_ORDER[CALLBACK_INTO_ORDER_FORMAT[callback_data]]
                created_order_id = NewOrderGetImportanceStep.get_created_order_id(data.from_user.id)
                if created_order_id is None:
                    create_order(data.from_user.id, important_name)
                    created_order_id = NewOrderGetImportanceStep.get_created_order_id(data.from_user.id)
                language_name = main_request.get_language_with_tg_id(data.from_user.id)
                states_views_object = StatesViews(language_name, data.from_user.id, created_order_id)
                return states_views_object.STATES_VIEWS[next_state]

        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id)
        return states_views_object.STATES_VIEWS[next_state]
    
    def view(self) -> None:
        """"""
        @self.dp.callback_query_handler(text = ButtonCallbackData.STANDART_IMPORTANCE_CALLBACK_DATA, state = self.state)
        async def standart_importance_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            """"""
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()

            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.NOW_IMPORTANCE_CALLBACK_DATA, state = self.state)
        async def now_importance_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            """"""
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()

            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.IMPORTANT_IMPORTANCE_CALLBACK_DATA, state = self.state)
        async def important_importance_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            """"""
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()

            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.VOLUMINOUS_IMPORTANCE_CALLBACK_DATA, state = self.state)
        async def voluminous_importance_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            """"""
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()

            await next_state.set()

        @self.dp.callback_query_handler(text = ButtonCallbackData.BACK_CALLBACK_DATA, state = self.state)
        async def back_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            """"""
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()

            await next_state.set()
        
        @self.dp.message_handler(state = self.state)
        async def client_main_menu_step_view(message: types.Message, state: FSMContext):
            view_object = Views("RUSSIAN", message.from_user.id)
            msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE
            await self.bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
            await message.answer(msg, reply_markup = keyboard)

    @property
    def action(self):
        self.view()