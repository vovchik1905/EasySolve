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
from settings.private.channel_config.channel_config import ChannelConfig


class CheckingUserSubscriptionStep(StepModel):
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        super().__init__(bot, dp, state)
    
    async def logic(self, data: Any) -> State:
        async def check_user_subscription(chat_id: int, user_id: int) -> bool:
            """Проверка подписался человек на группу или нет"""
            user_channel_obj = await self.bot.get_chat_member(chat_id, user_id)
            if user_channel_obj.status in ["creator", "administrator", "member"]:
                return True
            
            elif user_channel_obj.status == "restricted" and user_channel_obj.is_member:
                return True
            
            return False
        
        
        RuntimeStorageTelegram.tg_id = data.from_user.id
        subscript_value = await check_user_subscription(ChannelConfig.CHANNEL_TG_ID, RuntimeStorageTelegram.tg_id)
        if subscript_value:
            return BotStates.SETTING_UP_USER_LANGUAGE
        else:
            return BotStates.CHECKING_USER_SUBSCRIPTION_STEP
    
    async def db(self, next_state: State, data: Any) -> Any:
        language_name = "RUSSIAN"
        states_views_object = StatesViews(language_name, data.from_user.id)
        return states_views_object.STATES_VIEWS[next_state]
    
    def view(self) -> None:
        """"""
        @self.dp.callback_query_handler(text = ButtonCallbackData.USER_SUBSCRIPTION_CHECK_CALLBACK_DATA, state = self.state)
        async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            #await self.bot.answer_callback_query(callback_query.id)
            #await self.bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            if next_state is BotStates.SETTING_UP_USER_LANGUAGE:
                await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
                await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
                await callback_query.answer()
            else:
                await callback_query.answer(msg, show_alert=True)
            await next_state.set()
        
        #@self.dp.message_handler(state = self.state)
        #async def check_subscript_step_view(message: types.Message, state: FSMContext):
        #    next_state = await self.logic(message)
        #    output_data = await self.db(next_state, message)
        #    msg, keyboard = output_data
        #    await message.answer(msg, reply_markup = keyboard)
        #    await next_state.set()
        
    
    @property
    def action(self):
        self.view()