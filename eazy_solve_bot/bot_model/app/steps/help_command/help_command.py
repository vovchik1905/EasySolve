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
from bot_model.app.states.states import BotStates
from bot_model.app.step_models.views.views import Views


class HelpCommand(CommandModel):
    def __init__(self, bot: Bot, dp: Dispatcher, command: BotCommand, state: State = None) -> None:
        super().__init__(bot, dp, command, state)
    
    async def logic(self, data: Any) -> State:
        pass
    
    async def db(self, next_state: State, data: Any) -> Any:
        """"""
        try:
            language_name = main_request.get_language_with_tg_id(data.from_user.id)
        except:
            language_name = "RUSSIAN"
        
        states_views_object = StatesViews(language_name, data.from_user.id)
        return states_views_object.STATES_VIEWS[next_state]
    
    def view(self) -> None:
        @self.dp.message_handler(commands=self.command, state=BotStates.all_states)
        async def start_command_view(message: types.Message, state: FSMContext):
            """Тут написан дикий костыль, как по другому не знаю"""
            unparse_state_name = await state.get_state()
            state_name = unparse_state_name.split(":")[1]
            
            next_state = getattr(BotStates, state_name)
            output_data = await self.db(next_state, message)
            msg, keyboard = output_data
            try:
                language_name = main_request.get_language_with_tg_id(message.from_user.id)
            except:
                language_name = "RUSSIAN"
            views_object = Views(language_name, message.from_user.id)
            help_msg, help_kb = views_object.HELP_COMMAND_VIEW
            await self.bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
            await message.answer(help_msg, reply_markup=help_kb)
            await message.answer(msg, reply_markup=keyboard)
            await next_state.set()
    
    @property
    def action(self):
        self.view()