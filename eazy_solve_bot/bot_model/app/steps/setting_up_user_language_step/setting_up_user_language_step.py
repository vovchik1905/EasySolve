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


class SettingUpUserLanguageStep(StepModel):
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        super().__init__(bot, dp, state)
    
    async def logic(self, data: Any) -> State:
        #def get_or_none_user_language(data):
        #    language_name = data["data"]
        #    return language_request.get_or_none_language_id(language_name)
        active_languages = []
        for language in GeneralSettings.LANGUAGES:
            if GeneralSettings.LANGUAGES[language] is True:
                active_languages.append(language)
        #RuntimeStorageLanguage.name = get_or_none_user_language(data)
        RuntimeStorageLanguage.name = data["data"]
        if RuntimeStorageLanguage.name not in active_languages:
            return BotStates.SETTING_UP_USER_LANGUAGE
        else:
            if GeneralSettings.GET_CLIENT_TIME_ZONE:
                return BotStates.SETTING_UP_USER_TIME_ZONE
            return BotStates.CLIENT_MAIN_MENU
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #if не выполняется BAG
    
    async def db(self, next_state: State, data: Any) -> Any:
        """"""
        def create_client(data):

            RuntimeStorageTelegram.tg_id = data.from_user.id
            RuntimeStorageTelegram.tg_name = data.from_user.first_name
            RuntimeStorageTelegram.tg_sername = data.from_user.last_name
            RuntimeStorageTelegram.tg_username = data.from_user.username

            telegram_request.create_new_telegram(RuntimeStorageTelegram.tg_id,
                                                RuntimeStorageTelegram.tg_name,
                                                RuntimeStorageTelegram.tg_sername,
                                                RuntimeStorageTelegram.tg_username)
            RuntimeStorageUser.telegram = telegram_request.get_telegram_id(RuntimeStorageTelegram.tg_id)
            language_name = data["data"]
            RuntimeStorageUser.language = language_request.get_language_id(language_name)
            currency_name = GeneralSettings.CREATOR_SETTINGS["currency"]
            RuntimeStorageUser.currency = currency_request.get_currency_id(currency_name)
            RuntimeStorageUser.payment_info = payment_info_request.get_paiment_info_id(GeneralSettings.BASE_PAYMENT_INFO["card_number"])
            user_request.create_new_user(RuntimeStorageUser.telegram,
                                        RuntimeStorageUser.language,
                                        RuntimeStorageUser.currency,
                                        RuntimeStorageUser.payment_info)
        if next_state is BotStates.CLIENT_MAIN_MENU or next_state is BotStates.SETTING_UP_USER_TIME_ZONE:
            create_client(data)
            language_name = main_request.get_language_with_tg_id(data.from_user.id)
            states_views_object = StatesViews(language_name, data.from_user.id)
            return states_views_object.STATES_VIEWS[next_state]
        elif next_state is BotStates.SETTING_UP_USER_LANGUAGE:
            views_object = Views("RUSSIAN", data.from_user.id)
            return views_object.RESETTING_UP_USER_LANGUAGE_STEP
    
    def view(self) -> None:
        """"""
        @self.dp.callback_query_handler(text = ButtonCallbackData.RUSSIAN_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def russian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.CHINESE_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def chinese_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.ENGLISH_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def english_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.FRENCH_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def french_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.GERMAN_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def german_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.SPANISH_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def spanish_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.PORTUGUESE_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def portuguese_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.UKRAINIAN_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def ukrainian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
    
        @self.dp.callback_query_handler(text = ButtonCallbackData.BELARUSIAN_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def belarusian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.KAZAKH_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def kazakh_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()

        @self.dp.callback_query_handler(text = ButtonCallbackData.GEORGIAN_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def georgian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.ARMENIAN_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def armenian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.HEBREW_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def hebrew_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        
        @self.dp.callback_query_handler(text = ButtonCallbackData.TURKISH_LANGUAGE_CALLBACK_DATA, state = self.state)
        async def turkish_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
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