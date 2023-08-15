from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData
from bot_model.app.db.requests.order_request import order_request
from settings.general.order_format import OrderFormatEnum, ORDER_FORMAT


DONE_VALUE = "✅"


class AdditionalOrderSettingsMenuKeyboard:
    def __init__(self, language: str, order_id: int) -> None:
        def check_support_order(order_id: int):
            if order_request.get_order_support(order_id) is True:
                return True
            return False
        
        def check_percent_complet_order(order_id: int):
            if order_request.get_order_percent_complet(order_id) is not None:
                return True
            return False
        
        def check_preferred_budget_order(order_id: int):
            if order_request.get_order_preferred_budget(order_id) is not None:
                return True
            return False
        
        def check_type_order(order_id: int):
            order_format_name = order_request.get_order_format_name(order_id)
            if order_format_name is not None:
                if ORDER_FORMAT[order_request.get_order_format_name(order_id)] != OrderFormatEnum.NONE:
                    return True
            return False
        
        self.button_headings = ButtonHeadings(language)
        
        if check_support_order(order_id):
            support_order_setting_btn_heading = f"{self.button_headings.SUPPORT_ORDER_SETTING_HEADING}: {DONE_VALUE}"
        else:
            support_order_setting_btn_heading = self.button_headings.SUPPORT_ORDER_SETTING_HEADING

        if check_percent_complet_order(order_id):
            percent_complet_order_setting_btn_heading = f"{self.button_headings.PERCENT_COMPLET_ORDER_SETTING_HEADING}: {DONE_VALUE}"
        else:
            percent_complet_order_setting_btn_heading = self.button_headings.PERCENT_COMPLET_ORDER_SETTING_HEADING
        
        if check_preferred_budget_order(order_id):
            preferred_budget_order_setting_btn_heading = f"{self.button_headings.PREFERRED_BUDGET_ORDER_SETTING_HEADING}: {DONE_VALUE}"
        else:
            preferred_budget_order_setting_btn_heading = self.button_headings.PREFERRED_BUDGET_ORDER_SETTING_HEADING
        
        if check_type_order(order_id):
            type_order_setting_btn_heading = f"{self.button_headings.TYPE_ORDER_SETTING_HEADING}: {DONE_VALUE}"
        else:
            type_order_setting_btn_heading = self.button_headings.TYPE_ORDER_SETTING_HEADING

        self.support_order_setting_btn = InlineKeyboardButton(support_order_setting_btn_heading,
                                                            callback_data=ButtonCallbackData.SUPPORT_ORDER_SETTING_CALLBACK_DATA)

        self.percent_complet_order_setting_btn = InlineKeyboardButton(percent_complet_order_setting_btn_heading,
                                                                    callback_data=ButtonCallbackData.PERCENT_COMPLET_ORDER_SETTING_CALLBACK_DATA)

        self.preferred_budget_order_setting_btn = InlineKeyboardButton(preferred_budget_order_setting_btn_heading,
                                                                        callback_data=ButtonCallbackData.PREFERRED_BUDGET_ORDER_SETTING_CALLBACK_DATA)

        self.type_order_setting_btn = InlineKeyboardButton(type_order_setting_btn_heading,
                                                            callback_data=ButtonCallbackData.TYPE_ORDER_SETTING_CALLBACK_DATA)

        self.back_btn = InlineKeyboardButton(self.button_headings.BACK_HEADING,
                                                callback_data=ButtonCallbackData.BACK_CALLBACK_DATA)

        self.additional_order_settings_menu_keyboard = InlineKeyboardMarkup(row_width=2)
        self.additional_order_settings_menu_keyboard.add(self.support_order_setting_btn,
                                                        self.percent_complet_order_setting_btn,
                                                        self.preferred_budget_order_setting_btn,
                                                        self.type_order_setting_btn,
                                                        self.back_btn)