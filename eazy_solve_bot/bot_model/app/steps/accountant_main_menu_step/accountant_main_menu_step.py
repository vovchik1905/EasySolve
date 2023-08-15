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
from bot_model.app.states.states import BotStates
from bot_model.app.step_models.states_views import StatesViews
from settings.general.user_privileges import UserPrivileges, INT_TO_USER_PRIVILEGES
from bot_model.app.step_models.keyboards.button_headings import ButtonCallbackData
from bot_model.app.step_models.views.views import Views


class AccountantMainMenuStep(StepModel):
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        super().__init__(bot, dp, state)
    
    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        if callback_data == ButtonCallbackData.CUSTOM_MENU_CALLBACK_DATA:
            return BotStates.CLIENT_AND_SOLVER_MAIN_MENU
        elif callback_data == ButtonCallbackData.ACCOUNTANT_CONTROL_PANEL_CALLBACK_DATA:
            return BotStates.ACCOUNTANT_CONTROL_MENU
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id)
        return states_views_object.STATES_VIEWS[next_state]
    
    def view(self) -> None:
        @self.dp.callback_query_handler(text = ButtonCallbackData.CUSTOM_MENU_CALLBACK_DATA, state = self.state)
        async def custom_menu_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            """"""
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()

            await next_state.set()

        @self.dp.callback_query_handler(text = ButtonCallbackData.ACCOUNTANT_CONTROL_PANEL_CALLBACK_DATA, state = self.state)
        async def accountant_control_panel_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
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