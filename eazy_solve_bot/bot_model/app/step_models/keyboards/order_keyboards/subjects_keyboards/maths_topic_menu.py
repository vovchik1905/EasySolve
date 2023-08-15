from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


class MathsMenuKeyboard:
    def __init__(self, language: str) -> None:
        self.button_headings = ButtonHeadings(language)

        self.calculus_of_variations_topic_btn = InlineKeyboardButton(self.button_headings.CALCULUS_OF_VARIATIONS_HEADING,
                                                    callback_data=ButtonCallbackData.CALCULUS_OF_VARIATIONS_CALLBACK_DATA)   #+
        
        self.vector_tensor_analysis_topic_btn = InlineKeyboardButton(self.button_headings.VECTOR_TENSOR_ANALYSIS_HEADING,
                                                    callback_data=ButtonCallbackData.VECTOR_TENSOR_ANALYSIS_CALLBACK_DATA)   #+

        self.computational_mathematics_topic_btn = InlineKeyboardButton(self.button_headings.COMPUTATIONAL_MATHEMATICS_HEADING,
                                                    callback_data=ButtonCallbackData.COMPUTATIONAL_MATHEMATICS_CALLBACK_DATA)   #+

        self.discrete_mathematics_topic_btn = InlineKeyboardButton(self.button_headings.DISCRETE_MATHEMATICS_HEADING,
                                                    callback_data=ButtonCallbackData.DISCRETE_MATHEMATICS_CALLBACK_DATA)   #+
        
        self.diffusions_topic_btn = InlineKeyboardButton(self.button_headings.DIFFUSIONS_HEADING,
                                                    callback_data=ButtonCallbackData.DIFFUSIONS_CALLBACK_DATA)   #+

        self.multiple_integrals_topic_btn = InlineKeyboardButton(self.button_headings.MULTIPLE_INTEGRALS_HEADING,
                                                    callback_data=ButtonCallbackData.MULTIPLE_INTEGRALS_CALLBACK_DATA)   #+

        self.mathematical_analysis_topic_btn = InlineKeyboardButton(self.button_headings.MATHEMATICAL_ANALYSIS_HEADING,
                                                    callback_data=ButtonCallbackData.MATHEMATICAL_ANALYSIS_CALLBACK_DATA)   #+

        self.mathematical_modeling_topic_btn = InlineKeyboardButton(self.button_headings.MATHEMATICAL_MODELING_HEADING,
                                                    callback_data=ButtonCallbackData.MATHEMATICAL_MODELING_CALLBACK_DATA)   #+

        self.system_analysis_and_decision_making_topic_btn = InlineKeyboardButton(self.button_headings.SYSTEM_ANALYSIS_AND_DECISION_MAKING_HEADING,
                                                    callback_data=ButtonCallbackData.SYSTEM_ANALYSIS_AND_DECISION_MAKING_CALLBACK_DATA)   #+

        self.tfcp_topic_btn = InlineKeyboardButton(self.button_headings.TFCP_HEADING,
                                                    callback_data=ButtonCallbackData.TFCP_CALLBACK_DATA)   #+

        self.analytical_geometry_topic_btn = InlineKeyboardButton(self.button_headings.ANALYTICAL_GEOMETRY_HEADING,
                                                    callback_data=ButtonCallbackData.ANALYTICAL_GEOMETRY_CALLBACK_DATA)   #+

        self.linear_algebra_topic_btn = InlineKeyboardButton(self.button_headings.LINEAR_ALGEBRA_HEADING,
                                                    callback_data=ButtonCallbackData.LINEAR_ALGEBRA_CALLBACK_DATA)   #+

        self.mathematical_statistics_topic_btn = InlineKeyboardButton(self.button_headings.MATHEMATICAL_STATISTICS_HEADING,
                                                    callback_data=ButtonCallbackData.MATHEMATICAL_STATISTICS_CALLBACK_DATA)   #+

        self.rows_topic_btn = InlineKeyboardButton(self.button_headings.ROWS_HEADING,
                                                    callback_data=ButtonCallbackData.ROWS_CALLBACK_DATA)   #+

        self.probability_theory_topic_btn = InlineKeyboardButton(self.button_headings.PROBABILITY_THEORY_HEADING,
                                                    callback_data=ButtonCallbackData.PROBABILITY_THEORY_CALLBACK_DATA)   #+

        self.topology_topic_btn = InlineKeyboardButton(self.button_headings.TOPOLOGY_HEADING,
                                                    callback_data=ButtonCallbackData.TOPOLOGY_CALLBACK_DATA)   #+

        self.umf_topic_btn = InlineKeyboardButton(self.button_headings.UMF_HEADING,
                                                    callback_data=ButtonCallbackData.UMF_CALLBACK_DATA)   #+
        
        self.functional_analysis_topic_btn = InlineKeyboardButton(self.button_headings.FUNCTIONAL_ANALYSIS_HEADING,
                                                    callback_data=ButtonCallbackData.FUNCTIONAL_ANALYSIS_CALLBACK_DATA)   #+

        self.functions_of_multiple_variables_topic_btn = InlineKeyboardButton(self.button_headings.FUNCTIONS_OF_MULTIPLE_VARIABLES_HEADING,
                                                    callback_data=ButtonCallbackData.FUNCTIONS_OF_MULTIPLE_VARIABLES_CALLBACK_DATA)   #+

        self.other_maths_topic_btn = InlineKeyboardButton(self.button_headings.OTHER_MATHS_HEADING,
                                                    callback_data=ButtonCallbackData.OTHER_MATHS_CALLBACK_DATA)   #+


        self.maths_menu_keyboard = InlineKeyboardMarkup(row_width=1)
        self.maths_menu_keyboard.add(self.calculus_of_variations_topic_btn, self.vector_tensor_analysis_topic_btn,
                                    self.computational_mathematics_topic_btn, self.discrete_mathematics_topic_btn,
                                    self.diffusions_topic_btn, self.multiple_integrals_topic_btn,
                                    self.mathematical_analysis_topic_btn, self.mathematical_modeling_topic_btn,
                                    self.system_analysis_and_decision_making_topic_btn, self.tfcp_topic_btn,
                                    self.analytical_geometry_topic_btn, self.linear_algebra_topic_btn,
                                    self.mathematical_statistics_topic_btn, self.rows_topic_btn,
                                    self.probability_theory_topic_btn, self.topology_topic_btn,
                                    self.umf_topic_btn, self.functional_analysis_topic_btn,
                                    self.functions_of_multiple_variables_topic_btn, self.other_maths_topic_btn)