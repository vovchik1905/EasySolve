from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


ENGINEERING_GRAPHICS = "ENGINEERING_GRAPHICS"                                       #инженерная графика
DESCRIPTIVE_GEOMETRY = "DESCRIPTIVE_GEOMETRY"                                       #начертательная геометрия
CIRCUITRY_AND_MECHATRONICS = "CIRCUITRY_AND_MECHATRONICS"                           #схемотехника и мехатроника
THEORY_OF_MECHANISMS_AND_MACHINES = "THEORY_OF_MECHANISMS_AND_MACHINES"             #теория механизмов и машин
TECHNOLOGY_OF_STRUCTURAL_MATERIALS = "TECHNOLOGY_OF_STRUCTURAL_MATERIALS"           #технология конструкционных материалов
ELECTRONICS = "ELECTRONICS"                                                         #электроника
ELECTRONIC_BOARDS_AND_COMPONENTS = "ELECTRONIC_BOARDS_AND_COMPONENTS"               #электронные платы и компоненты
ELECTRICAL_ENGINEERING = "ELECTRICAL_ENGINEERING"                                   #электротехника
ANALYTICAL_MECHANICS = "ANALYTICAL_MECHANICS"                                       #аналитическая механика
MACHINES = "MACHINES"                                                               #станки
OTHER_ENGINEERING = "OTHER_ENGINEERING"

class EngineeringMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.engineering_graphics_topic_btn = InlineKeyboardButton(self.button_headings.ENGINEERING_GRAPHICS_HEADING,
                                                    callback_data=ButtonCallbackData.ENGINEERING_GRAPHICS_CALLBACK_DATA)   #+
        
        self.descriptive_geometry_topic_btn = InlineKeyboardButton(self.button_headings.DESCRIPTIVE_GEOMETRY_HEADING,
                                                    callback_data=ButtonCallbackData.DESCRIPTIVE_GEOMETRY_CALLBACK_DATA)   #+

        self.circuitry_and_mechatronics_topic_btn = InlineKeyboardButton(self.button_headings.CIRCUITRY_AND_MECHATRONICS_HEADING,
                                                    callback_data=ButtonCallbackData.CIRCUITRY_AND_MECHATRONICS_CALLBACK_DATA)   #+

        self.theory_of_mechanisms_and_machines_topic_btn = InlineKeyboardButton(self.button_headings.THEORY_OF_MECHANISMS_AND_MACHINES_HEADING,
                                                    callback_data=ButtonCallbackData.THEORY_OF_MECHANISMS_AND_MACHINES_CALLBACK_DATA)   #+
        
        self.technology_of_structural_materials_topic_btn = InlineKeyboardButton(self.button_headings.TECHNOLOGY_OF_STRUCTURAL_MATERIALS_HEADING,
                                                    callback_data=ButtonCallbackData.TECHNOLOGY_OF_STRUCTURAL_MATERIALS_CALLBACK_DATA)   #+

        self.electronics_topic_btn = InlineKeyboardButton(self.button_headings.ELECTRONICS_HEADING,
                                                    callback_data=ButtonCallbackData.ELECTRONICS_CALLBACK_DATA)   #+

        self.electronic_boards_and_components_topic_btn = InlineKeyboardButton(self.button_headings.ELECTRONIC_BOARDS_AND_COMPONENTS_HEADING,
                                                    callback_data=ButtonCallbackData.ELECTRONIC_BOARDS_AND_COMPONENTS_CALLBACK_DATA)   #+

        self.electrical_engineering_topic_btn = InlineKeyboardButton(self.button_headings.ELECTRICAL_ENGINEERING_HEADING,
                                                    callback_data=ButtonCallbackData.ELECTRICAL_ENGINEERING_CALLBACK_DATA)   #+

        self.analytical_mechanics_topic_btn = InlineKeyboardButton(self.button_headings.ANALYTICAL_MECHANICS_HEADING,
                                                    callback_data=ButtonCallbackData.ANALYTICAL_MECHANICS_CALLBACK_DATA)   #+

        self.machines_topic_btn = InlineKeyboardButton(self.button_headings.MACHINES_HEADING,
                                                    callback_data=ButtonCallbackData.MACHINES_CALLBACK_DATA)   #+

        self.other_engineering_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_ENGINEERING_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_ENGINEERING_CALLBACK_DATA)   #+

        
        self.engineering_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.engineering_menu_keyboard.add(self.engineering_graphics_topic_btn, self.descriptive_geometry_topic_btn,
                                    self.circuitry_and_mechatronics_topic_btn, self.theory_of_mechanisms_and_machines_topic_btn,
                                    self.technology_of_structural_materials_topic_btn, self.electronics_topic_btn,
                                    self.electronic_boards_and_components_topic_btn, self.electrical_engineering_topic_btn,
                                    self.analytical_mechanics_topic_btn, self.machines_topic_btn,
                                    self.other_engineering_topic_btn)