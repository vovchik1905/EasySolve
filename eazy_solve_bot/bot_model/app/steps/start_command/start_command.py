from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State
from aiogram import types
from aiogram.dispatcher import FSMContext
from typing import Any

from bot_model.app.db.runtime_storage.runtime_storage import *
from bot_model.app.step_models.commands.bot_commands import BotCommand
from bot_model.app.step_models.command_model import CommandModel
from bot_model.app.step_models.messages.messages import Messages
from bot_model.app.db.requests.telegram_requests import TelegramRequests, telegram_request
from bot_model.app.db.requests.user_requests import UserRequests, user_request
from bot_model.app.db.requests.main_requests import MainRequests, main_request
from bot_model.app.states.states import BotStates
from bot_model.app.step_models.states_views import StatesViews
from settings.general.user_privileges import UserPrivileges, INT_TO_USER_PRIVILEGES
from bot_model.app.step_models.views.views import Views


class StartCommand(CommandModel):
    def __init__(self, bot: Bot, dp: Dispatcher, command: BotCommand, state: State = None) -> None:
        super().__init__(bot, dp, command, state)
    
    
    async def logic(self, data: Any) -> State:
        def get_telegram_id(msg: Any) -> Any:
            RuntimeStorageTelegram.tg_id = msg.from_user.id
            return telegram_request.get_or_none_telegram_id(RuntimeStorageTelegram.tg_id)
        
        def get_user_privileges(user_telegram: int) -> int:
            RuntimeStorageUser.telegram = user_telegram
            if RuntimeStorageUser.telegram is None:
                return None
            else:
                RuntimeStorageUser.id = user_request.get_user_id(RuntimeStorageUser.telegram)
                return user_request.get_user_privileges(RuntimeStorageUser.id)
        
        RuntimeStorageUser.privileges = get_user_privileges(get_telegram_id(data))
        if RuntimeStorageUser.privileges is None:
            return BotStates.CHECKING_USER_SUBSCRIPTION_STEP
        
        elif INT_TO_USER_PRIVILEGES[RuntimeStorageUser.privileges] is UserPrivileges.CLIENT:
            return BotStates.CLIENT_MAIN_MENU

        elif INT_TO_USER_PRIVILEGES[RuntimeStorageUser.privileges] is UserPrivileges.CLIENT_AND_SOLVER:
            return BotStates.CLIENT_AND_SOLVER_MAIN_MENU

        elif INT_TO_USER_PRIVILEGES[RuntimeStorageUser.privileges] is UserPrivileges.PARTNER:
            return BotStates.PARTNER_MAIN_MENU

        elif INT_TO_USER_PRIVILEGES[RuntimeStorageUser.privileges] is UserPrivileges.ADMIN:
            return BotStates.ADMIN_MAIN_MENU

        elif INT_TO_USER_PRIVILEGES[RuntimeStorageUser.privileges] is UserPrivileges.ACCOUNTANT:
            return BotStates.ACCOUNTANT_MAIN_MENU

        elif INT_TO_USER_PRIVILEGES[RuntimeStorageUser.privileges] is UserPrivileges.CREATOR:
            return BotStates.CREATOR_MAIN_MENU
    
    async def db(self, next_state: State, data: Any) -> Any:
        """"""
        if next_state is BotStates.CHECKING_USER_SUBSCRIPTION_STEP:
            language_name = "RUSSIAN"
            states_views_obj = StatesViews(language_name, data.from_user.id)
            return states_views_obj.STATES_VIEWS[next_state]

        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id)
        
        return states_views_object.STATES_VIEWS[next_state]

    def view(self) -> None:
        @self.dp.message_handler(commands=self.command)
        async def start_command_view(message: types.Message, state: FSMContext):
            next_state = await self.logic(message)
            output_data = await self.db(next_state, message)
            msg, keyboard = output_data
            
            await message.answer(msg, reply_markup=keyboard)
            await next_state.set()

    @property
    def action(self):
        self.view()
