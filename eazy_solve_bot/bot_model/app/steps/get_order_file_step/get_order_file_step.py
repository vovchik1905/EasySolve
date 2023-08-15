from datetime import datetime
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
from bot_model.app.db.requests.file_requests import file_request
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


ORDER_FILES_CALLBACK_DATA = [ButtonCallbackData.CONFIRM_FILES_CALLBACK_DATA,
                            ButtonCallbackData.DELETE_ALL_FILES_CALLBACK_DATA,
                            ButtonCallbackData.BACK_CALLBACK_DATA]


class GetOrderFilesStep(StepModel):
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        super().__init__(bot, dp, state)
    
    @staticmethod
    def check_order_file(file_msg: Any) -> bool:
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
    def create_created_order_file(tg_id: int, order_file_id: str) -> Any:
        created_order_id = GetOrderFilesStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        file_datetime = datetime.today()
        file_request.create_file(created_order_id, order_file_id, file_datetime_get=file_datetime)
        #order_request.update_order_comment(created_order_id, order_file_id)
        return created_order_id
    
    @staticmethod
    def delete_all_created_order_files(created_order_id: int) -> None:
        file_request.delete_all_order_files(created_order_id)

    @staticmethod
    def check_created_order_files_quantity(created_order_id: int) -> bool:
        files_num = file_request.get_order_files_num(created_order_id)
        if files_num < GeneralSettings.ORDER_FILES_QUANTITY_LIMIT:
            return True
        return False

    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = GetOrderFilesStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name

    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        if callback_data in [ButtonCallbackData.CONFIRM_FILES_CALLBACK_DATA, ButtonCallbackData.BACK_CALLBACK_DATA]:
            order_importance = GetOrderFilesStep.get_order_importance(data.from_user.id)
            if ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.STANDARD:
                return BotStates.MAIN_STANDART_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.NOW:
                return BotStates.MAIN_NOW_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.IMPORTANT:
                return BotStates.MAIN_IMPORTANT_ORDER_MENU_STEP
            elif ORDER_IMPORTANCE[order_importance] is OrderImportanceEnum.VOLUMINOUS:
                return BotStates.MAIN_VOLUMINOUS_ORDER_MENU_STEP
        return self.state
    
    async def db(self, next_state: State, data: Any) -> Any:
        callback_data = data["data"]
        order_id = GetOrderFilesStep.get_created_order_id(data.from_user.id)
        if callback_data == ButtonCallbackData.DELETE_ALL_FILES_CALLBACK_DATA:
            GetOrderFilesStep.delete_all_created_order_files(order_id)
        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id, order_id)
        return states_views_object.STATES_VIEWS[next_state]

    def view(self) -> None:
        @self.dp.callback_query_handler(lambda call: call.data in ORDER_FILES_CALLBACK_DATA, state = self.state)
        async def russian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            if callback_query["data"] == ButtonCallbackData.DELETE_ALL_FILES_CALLBACK_DATA:
                language_name = main_request.get_language_with_tg_id(callback_query.from_user.id)
                message_object = Messages(language_name)
                msg1 = message_object.DELETE_ALL_ORDER_FILES_MESSAGE
                await self.bot.send_message(callback_query.from_user.id, msg1)
            await callback_query.answer()
            await next_state.set()


        @self.dp.message_handler(state = self.state, content_types = [*types.ContentTypes.VIDEO,
                                                                        *types.ContentTypes.PHOTO,
                                                                        *types.ContentTypes.DOCUMENT,
                                                                        *types.ContentTypes.AUDIO,
                                                                        *types.ContentTypes.VOICE,
                                                                        *types.ContentTypes.VIDEO_NOTE,
                                                                        *types.ContentTypes.ANIMATION])
        async def setting_up_language_step_view(message: types.Message, state: FSMContext):
            order_id = GetOrderFilesStep.get_created_order_id(message.from_user.id)
            language_name = main_request.get_language_with_tg_id(message.from_user.id)
            if GetOrderFilesStep.check_created_order_files_quantity(order_id):
                if GetOrderFilesStep.check_order_file(message):
                    video = message.video.file_id if message.video else None
                    photo = message.photo[-1].file_id if message.photo else None
                    document = message.document.file_id if message.document else None
                    audio = message.audio.file_id if message.audio else None
                    voice = message.voice.file_id if message.voice else None
                    video_note = message.video_note.file_id if message.video_note else None
                    animation = message.animation.file_id if message.animation else None
                    #print(message)
                    if video is not None:
                        file_id = video
                    elif photo is not None:
                        file_id = photo
                    elif document is not None:
                        file_id = document
                    elif audio is not None:
                        file_id = audio
                    elif voice is not None:
                        file_id = voice
                    elif video_note is not None:
                        file_id = video_note
                    elif animation is not None:
                        file_id = animation
                    GetOrderFilesStep.create_created_order_file(message.from_user.id, file_id)
                    message_object = Messages(language_name)
                    msg1 = message_object.ORDER_FILE_ADDED_MESSAGE
                else:
                    message_object = Messages(language_name)
                    msg1 = message_object.ORDER_INVALID_FILE_MESSAGE
            else:
                message_object = Messages(language_name)
                msg1 = message_object.EXCEEDED_THE_ALLOWED_LIMIT_OF_ORDER_FILES_MESSAGE
            states_views_object = StatesViews(language_name, message.from_user.id, order_id)
            msg, keyboard = states_views_object.STATES_VIEWS[self.state]
            #bot_msg = await message.answer("")
            await self.bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
            #await self.bot.delete_message(chat_id=message.from_user.id, message_id=bot_msg.message_id)
            await self.bot.send_message(message.from_user.id, msg1)
            await self.bot.send_message(message.from_user.id, msg, reply_markup = keyboard)


        @self.dp.message_handler(state = self.state)
        async def setting_up_language_step_view(message: types.Message, state: FSMContext):
            view_object = Views("RUSSIAN", message.from_user.id)
            msg, keyboard = view_object.BAD_USER_ANSWER_MESSAGE
            await message.answer(msg, reply_markup = keyboard)

    @property
    def action(self):
        self.view()