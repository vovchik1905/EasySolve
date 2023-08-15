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
from settings.general.order_importance import OrderImportanceEnum, IMPORTANCE_ORDER, ORDER_IMPORTANCE
from bot_model.app.db.requests.order_request import OrderRequests, order_request
from settings.general.order_topic import ORDER_TOPIC
from bot_model.app.step_models.messages.messages import Messages
from bot_model.app.step_models.views.views import Views


#"""
ORDER_TOPIC_CALLBACK_DATA = [ButtonCallbackData.CALCULUS_OF_VARIATIONS_CALLBACK_DATA,
                            ButtonCallbackData.VECTOR_TENSOR_ANALYSIS_CALLBACK_DATA,
                            ButtonCallbackData.COMPUTATIONAL_MATHEMATICS_CALLBACK_DATA,
                            ButtonCallbackData.DISCRETE_MATHEMATICS_CALLBACK_DATA,
                            ButtonCallbackData.DIFFUSIONS_CALLBACK_DATA,
                            ButtonCallbackData.MULTIPLE_INTEGRALS_CALLBACK_DATA,
                            ButtonCallbackData.MATHEMATICAL_ANALYSIS_CALLBACK_DATA,
                            ButtonCallbackData.MATHEMATICAL_MODELING_CALLBACK_DATA,
                            ButtonCallbackData.SYSTEM_ANALYSIS_AND_DECISION_MAKING_CALLBACK_DATA,
                            ButtonCallbackData.TFCP_CALLBACK_DATA,
                            ButtonCallbackData.ANALYTICAL_GEOMETRY_CALLBACK_DATA,
                            ButtonCallbackData.LINEAR_ALGEBRA_CALLBACK_DATA,
                            ButtonCallbackData.MATHEMATICAL_STATISTICS_CALLBACK_DATA,
                            ButtonCallbackData.ROWS_CALLBACK_DATA,
                            ButtonCallbackData.PROBABILITY_THEORY_CALLBACK_DATA,
                            ButtonCallbackData.TOPOLOGY_CALLBACK_DATA,
                            ButtonCallbackData.UMF_CALLBACK_DATA,
                            ButtonCallbackData.FUNCTIONAL_ANALYSIS_CALLBACK_DATA,
                            ButtonCallbackData.FUNCTIONS_OF_MULTIPLE_VARIABLES_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_MATHS_CALLBACK_DATA,
                            ButtonCallbackData.QUANTUM_MECHANICS_CALLBACK_DATA,
                            ButtonCallbackData.MATERIALS_SCIENCE_CALLBACK_DATA,
                            ButtonCallbackData.METROLOGY_CALLBACK_DATA,
                            ButtonCallbackData.MECHANICS_CALLBACK_DATA,
                            ButtonCallbackData.FLUID_AND_GAS_MECHANICS_CALLBACK_DATA,
                            ButtonCallbackData.OPTICS_CALLBACK_DATA,
                            ButtonCallbackData.STRENGTH_OF_MATERIALS_CALLBACK_DATA,
                            ButtonCallbackData.THEORETICAL_MECHANICS_CALLBACK_DATA,
                            ButtonCallbackData.ELECTRICITY_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_PHYSICS_CALLBACK_DATA,
                            ButtonCallbackData.BASIC_IT_CALLBACK_DATA,
                            ButtonCallbackData.C_IT_CALLBACK_DATA,
                            ButtonCallbackData.C_SHARP_IT_CALLBACK_DATA,
                            ButtonCallbackData.C_PLUS_PLUS_IT_CALLBACK_DATA,
                            ButtonCallbackData.DELPHI_IT_CALLBACK_DATA,
                            ButtonCallbackData.EXCEL_IT_CALLBACK_DATA,
                            ButtonCallbackData.JAVA_IT_CALLBACK_DATA,
                            ButtonCallbackData.JAVA_SCRIPT_CALLBACK_DATA,
                            ButtonCallbackData.GO_IT_CALLBACK_DATA,
                            ButtonCallbackData.MATLAB_IT_CALLBACK_DATA,
                            ButtonCallbackData.PYTHON_IT_CALLBACK_DATA,
                            ButtonCallbackData.PHP_IT_CALLBACK_DATA,
                            ButtonCallbackData.DATA_BASE_IT_CALLBACK_DATA,
                            ButtonCallbackData.LATEX_IT_CALLBACK_DATA,
                            ButtonCallbackData.LAZARUS_CALLBACK_DATA,
                            ButtonCallbackData.PASCAL_IT_CALLBACK_DATA,
                            ButtonCallbackData.R_IT_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_IT_CALLBACK_DATA,
                            ButtonCallbackData.ENGINEERING_GRAPHICS_CALLBACK_DATA,
                            ButtonCallbackData.DESCRIPTIVE_GEOMETRY_CALLBACK_DATA,
                            ButtonCallbackData.CIRCUITRY_AND_MECHATRONICS_CALLBACK_DATA,
                            ButtonCallbackData.THEORY_OF_MECHANISMS_AND_MACHINES_CALLBACK_DATA,
                            ButtonCallbackData.TECHNOLOGY_OF_STRUCTURAL_MATERIALS_CALLBACK_DATA,
                            ButtonCallbackData.ELECTRONICS_CALLBACK_DATA,
                            ButtonCallbackData.ELECTRONIC_BOARDS_AND_COMPONENTS_CALLBACK_DATA,
                            ButtonCallbackData.ELECTRICAL_ENGINEERING_CALLBACK_DATA,
                            ButtonCallbackData.ANALYTICAL_MECHANICS_CALLBACK_DATA,
                            ButtonCallbackData.MACHINES_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_ENGINEERING_CALLBACK_DATA,
                            ButtonCallbackData.LOGISTICS_CALLBACK_DATA,
                            ButtonCallbackData.MACROECONOMICS_CALLBACK_DATA,
                            ButtonCallbackData.MARKETING_CALLBACK_DATA,
                            ButtonCallbackData.MANAGEMENT_CALLBACK_DATA,
                            ButtonCallbackData.MICROECONOMICS_CALLBACK_DATA,
                            ButtonCallbackData.TAXATION_CALLBACK_DATA,
                            ButtonCallbackData.PERSONNEL_MANAGEMENT_CALLBACK_DATA,
                            ButtonCallbackData.ECONOMY_CALLBACK_DATA,
                            ButtonCallbackData.ACCOUNTING_CALLBACK_DATA,
                            ButtonCallbackData.ECONOMETRICS_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_ECONOMY_CALLBACK_DATA,
                            ButtonCallbackData.ORGANIC_CHEMISTRY_CALLBACK_DATA,
                            ButtonCallbackData.ANALYTICAL_CHEMISTRY_CALLBACK_DATA,
                            ButtonCallbackData.GENERAL_CHEMISTRY_CALLBACK_DATA,
                            ButtonCallbackData.BIOCHEMISTRY_CALLBACK_DATA,
                            ButtonCallbackData.PHYSICAL_CHEMISTRY_CALLBACK_DATA,
                            ButtonCallbackData.INORGANIC_CHEMISTRY_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_CHEMISTRY_CALLBACK_DATA,
                            ButtonCallbackData.RUSSIAN_CALLBACK_DATA,
                            ButtonCallbackData.CHINESE_CALLBACK_DATA,
                            ButtonCallbackData.ENGLISH_CALLBACK_DATA,
                            ButtonCallbackData.FRENCH_CALLBACK_DATA,
                            ButtonCallbackData.GERMAN_CALLBACK_DATA,
                            ButtonCallbackData.SPANISH_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_LANGUAGES_CALLBACK_DATA,
                            ButtonCallbackData.ANATOMY_CALLBACK_DATA,
                            ButtonCallbackData.PARASITOLOGY_CALLBACK_DATA,
                            ButtonCallbackData.BIOINFORMATICS_CALLBACK_DATA,
                            ButtonCallbackData.MICROBIOLOGY_CALLBACK_DATA,
                            ButtonCallbackData.BOTANY_CALLBACK_DATA,
                            ButtonCallbackData.MOLECULAR_BIOLOGY_CALLBACK_DATA,
                            ButtonCallbackData.ZOOLOGY_CALLBACK_DATA,
                            ButtonCallbackData.GENETICS_CALLBACK_DATA,
                            ButtonCallbackData.VIROLOGY_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_BIOLOGY_CALLBACK_DATA,
                            ButtonCallbackData.GEOGRAPHY_CALLBACK_DATA,
                            ButtonCallbackData.HISTORY_CALLBACK_DATA,
                            ButtonCallbackData.DESIGN_CALLBACK_DATA,
                            ButtonCallbackData.OBZH_CALLBACK_DATA,
                            ButtonCallbackData.PHILOSOPHY_CALLBACK_DATA,
                            ButtonCallbackData.LAW_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_HUMANITARIAN_CALLBACK_DATA,
                            ButtonCallbackData.REGISTRATION_CALLBACK_DATA]
#"""

ORDER_TOPICS_NAMES = [sbj_name for sbj_name in ORDER_TOPIC]
CALLBACK_DATA_INTO_TOPIC_NAME = {ORDER_TOPIC_CALLBACK_DATA[i]: ORDER_TOPICS_NAMES[i+1] for i in range(len(ORDER_TOPIC_CALLBACK_DATA))}

OTHER_TOPIC_CALLBACK_DATA = [ButtonCallbackData.OTHER_MATHS_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_PHYSICS_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_IT_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_ENGINEERING_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_ECONOMY_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_CHEMISTRY_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_LANGUAGES_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_BIOLOGY_CALLBACK_DATA,
                            ButtonCallbackData.OTHER_HUMANITARIAN_CALLBACK_DATA]

class GetOrderTopicStep(StepModel):
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
    def update_created_order_topic(tg_id: int, order_topic_name: str) -> Any:
        created_order_id = GetOrderTopicStep.get_created_order_id(tg_id)
        if created_order_id is None:
            return None
        order_topic_id = order_request.get_order_topic_id(order_topic_name)
        order_request.update_order_topic(created_order_id, order_topic_id)
        return created_order_id
    
    @staticmethod
    def get_order_importance(tg_id: int) -> Any:
        created_order_id = GetOrderTopicStep.get_created_order_id(tg_id)
        order_importance_name = order_request.get_order_importance_name_with_order_id(created_order_id)
        return order_importance_name
    
    async def logic(self, data: Any) -> State:
        callback_data = data["data"]
        if callback_data in ORDER_TOPIC_CALLBACK_DATA or callback_data in OTHER_TOPIC_CALLBACK_DATA:
            order_importance = GetOrderTopicStep.get_order_importance(data.from_user.id)
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
        order_topic = CALLBACK_DATA_INTO_TOPIC_NAME[callback_data]
        GetOrderTopicStep.update_created_order_topic(data.from_user.id, order_topic)
        order_id = GetOrderTopicStep.get_created_order_id(data.from_user.id)
        language_name = main_request.get_language_with_tg_id(data.from_user.id)
        states_views_object = StatesViews(language_name, data.from_user.id, order_id)
        return states_views_object.STATES_VIEWS[next_state]

    
    def view(self) -> None:
        @self.dp.callback_query_handler(lambda call: call.data in ORDER_TOPIC_CALLBACK_DATA, state = self.state)
        async def russian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, msg, reply_markup = keyboard)
            await callback_query.answer()
            await next_state.set()
        

        @self.dp.callback_query_handler(lambda call: call.data in OTHER_TOPIC_CALLBACK_DATA, state = self.state)
        async def russian_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
            next_state = await self.logic(callback_query)
            output_data = await self.db(next_state, callback_query)
            msg, keyboard = output_data
            await self.bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
            await self.bot.send_message(callback_query.from_user.id, Messages.GET_ORDER_OTHER_TOPIC)
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