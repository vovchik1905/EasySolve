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



TIME_ZONE_CALLBACK_DATA = [ButtonCallbackData.TIME_ZONE_UTC_MINUS12_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS11_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS10_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS09_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS08_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS07_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS06_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS05_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS04_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS03_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS02_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_MINUS01_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS00_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS01_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS02_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS03_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS04_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS05_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS06_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS07_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS08_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS09_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS10_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS11_CALLBACK_DATA,
                                    ButtonCallbackData.TIME_ZONE_UTC_PLUS12_CALLBACK_DATA]

TIME_ZONE_NAMES = [tz_name for tz_name in GeneralSettings.TIME_ZONES]

CALLBACK_INTO_TIME_ZONE = {TIME_ZONE_CALLBACK_DATA[i]: TIME_ZONE_NAMES[i] for i in range(len(TIME_ZONE_CALLBACK_DATA))}



class SettingUpUserTimeZoneStep(StepModel):
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        super().__init__(bot, dp, state)
    
    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        
        if callback_data in TIME_ZONE_CALLBACK_DATA:
            return BotStates.CLIENT_MAIN_MENU
        
        else:
            return BotStates.SETTING_UP_USER_TIME_ZONE
    
    async def db(self, next_state: State, data: Any) -> Any:
        callback_data = data["data"]
        def update_user_time_zone(tg_id: int, user_time_zone: str):
            RuntimeStorageTelegram.tg_id = tg_id
            RuntimeStorageUser.telegram = telegram_request.get_telegram_id(RuntimeStorageTelegram.tg_id)
            RuntimeStorageUser.id = user_request.get_user_id(RuntimeStorageUser.telegram)
            RuntimeStorageUser.time_zone = main_request.get_time_zone_id(user_time_zone)
            user_request.update_user_time_zone(RuntimeStorageUser.id, RuntimeStorageUser.time_zone)
        
        if next_state is BotStates.CLIENT_MAIN_MENU:
            update_user_time_zone(data.from_user.id, CALLBACK_INTO_TIME_ZONE[callback_data])
        
        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id)
        return states_views_object.STATES_VIEWS[next_state]

    
    def view(self) -> None:
        @self.dp.callback_query_handler(lambda call: call.data in TIME_ZONE_CALLBACK_DATA, state = self.state)
        #@self.dp.callback_query_handler(text = [], state = self.state)
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