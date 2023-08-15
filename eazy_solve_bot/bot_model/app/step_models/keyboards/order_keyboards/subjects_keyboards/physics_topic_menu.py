from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class PhysicsMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.quantum_mechanics_topic_btn = InlineKeyboardButton(self.button_headings.QUANTUM_MECHANICS_HEADING,
                                                    callback_data=ButtonCallbackData.QUANTUM_MECHANICS_CALLBACK_DATA)   #+
        
        self.materials_science_topic_btn = InlineKeyboardButton(self.button_headings.MATERIALS_SCIENCE_HEADING,
                                                    callback_data=ButtonCallbackData.MATERIALS_SCIENCE_CALLBACK_DATA)   #+

        self.metrology_topic_btn = InlineKeyboardButton(self.button_headings.METROLOGY_HEADING,
                                                    callback_data=ButtonCallbackData.METROLOGY_CALLBACK_DATA)   #+

        self.mechanics_topic_btn = InlineKeyboardButton(self.button_headings.MECHANICS_HEADING,
                                                    callback_data=ButtonCallbackData.MECHANICS_CALLBACK_DATA)   #+
        
        self.fluid_and_gas_mechanics_topic_btn = InlineKeyboardButton(self.button_headings.FLUID_AND_GAS_MECHANICS_HEADING,
                                                    callback_data=ButtonCallbackData.FLUID_AND_GAS_MECHANICS_CALLBACK_DATA)   #+

        self.optics_topic_btn = InlineKeyboardButton(self.button_headings.OPTICS_HEADING,
                                                    callback_data=ButtonCallbackData.OPTICS_CALLBACK_DATA)   #+

        self.strength_of_materials_topic_btn = InlineKeyboardButton(self.button_headings.STRENGTH_OF_MATERIALS_HEADING,
                                                    callback_data=ButtonCallbackData.STRENGTH_OF_MATERIALS_CALLBACK_DATA)   #+

        self.theoretical_mechanics_topic_btn = InlineKeyboardButton(self.button_headings.THEORETICAL_MECHANICS_HEADING,
                                                    callback_data=ButtonCallbackData.THEORETICAL_MECHANICS_CALLBACK_DATA)   #+

        self.electricity_topic_btn = InlineKeyboardButton(self.button_headings.ELECTRICITY_HEADING,
                                                    callback_data=ButtonCallbackData.ELECTRICITY_CALLBACK_DATA)   #+

        self.other_physics_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_PHYSICS_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_PHYSICS_CALLBACK_DATA)   #+

        
        self.physics_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.physics_menu_keyboard.add(self.quantum_mechanics_topic_btn, self.materials_science_topic_btn,
                                    self.metrology_topic_btn, self.mechanics_topic_btn,
                                    self.fluid_and_gas_mechanics_topic_btn, self.optics_topic_btn,
                                    self.strength_of_materials_topic_btn, self.theoretical_mechanics_topic_btn,
                                    self.electricity_topic_btn, self.other_physics_topic_btn)