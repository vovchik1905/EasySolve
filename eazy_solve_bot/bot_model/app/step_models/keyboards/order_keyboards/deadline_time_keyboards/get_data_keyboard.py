from typing import Any
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import datetime
from calendar import monthrange
from bot_model.app.step_models.keyboards.button_headings import ButtonHeadings, ButtonCallbackData


MONTH_LIST = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
WEEKDAY_LIST = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]


class DayNumber():
    DAY_CALLBACK_DATA = ButtonCallbackData.DAY_CALLBACK_DATA
    def __init__(self, year: int, month: int, day: int) -> None:
        self.num = day
        if self.num % 10 == 0:
            day_heading = f" {str(day)}"
        else:
            day_heading = str(day)
        self.day_obj = InlineKeyboardButton(day_heading, callback_data=f"{DayNumber.DAY_CALLBACK_DATA}_{day}")


class GetDateMenuKeyboard:
    """"""
    def __init__(self, language: str, year: int, month: int, day: int) -> None:
        #print(f"date: {year}.{month}.{day}")
        self.button_headings = ButtonHeadings(language)

        self.last_month_btn = InlineKeyboardButton("<===", callback_data=ButtonCallbackData.LAST_MONTH_CALLBACK_DATA)

        self.this_month_btn = InlineKeyboardButton(MONTH_LIST[month-1], callback_data=ButtonCallbackData.THIS_MONTH_CALLBACK_DATA)

        self.next_month_btn = InlineKeyboardButton("===>", callback_data=ButtonCallbackData.NEXT_MONTH_CALLBACK_DATA)

        self.monday_btn = InlineKeyboardButton(WEEKDAY_LIST[0], callback_data=ButtonCallbackData.WEEKDAY_CALLBACK_DATA)

        self.tuesday_btn = InlineKeyboardButton(WEEKDAY_LIST[1], callback_data=ButtonCallbackData.WEEKDAY_CALLBACK_DATA)

        self.wednesday_btn = InlineKeyboardButton(WEEKDAY_LIST[2], callback_data=ButtonCallbackData.WEEKDAY_CALLBACK_DATA)

        self.thursday_btn = InlineKeyboardButton(WEEKDAY_LIST[3], callback_data=ButtonCallbackData.WEEKDAY_CALLBACK_DATA)

        self.friday_btn = InlineKeyboardButton(WEEKDAY_LIST[4], callback_data=ButtonCallbackData.WEEKDAY_CALLBACK_DATA)

        self.saturday_btn = InlineKeyboardButton(WEEKDAY_LIST[5], callback_data=ButtonCallbackData.WEEKDAY_CALLBACK_DATA)

        self.sunday_btn = InlineKeyboardButton(WEEKDAY_LIST[6], callback_data=ButtonCallbackData.WEEKDAY_CALLBACK_DATA)

        self.none_day_btn = InlineKeyboardButton("  ", callback_data=ButtonCallbackData.NONE_DAY_CALLBACK_DATA)

        self.days_date_list = [DayNumber(year, month, i).day_obj for i in range(1,32)]

        def get_weekday(year: int, month: int, day: int) -> Any:
            try:
                now_data = datetime.date(year, month, day)
                return now_data.weekday()
            except ValueError as error:
                return None

        self.get_date_menu_keyboard = InlineKeyboardMarkup(row_width=7)

        self.get_date_menu_keyboard.row(self.last_month_btn, self.this_month_btn, self.next_month_btn)

        self.get_date_menu_keyboard.row(self.monday_btn,
                                        self.tuesday_btn,
                                        self.wednesday_btn,
                                        self.thursday_btn,
                                        self.friday_btn,
                                        self.saturday_btn,
                                        self.sunday_btn)

        month_len = monthrange(year, month)[1]
        calendar = self.days_date_list[day-1:month_len]
        weekday_difference = get_weekday(year, month, day)
        for i in range(weekday_difference):
            calendar.insert(0, self.none_day_btn)
        
        weekday_difference = 6 - get_weekday(year, month, month_len)
        for j in range(weekday_difference):
            calendar.append(self.none_day_btn)
        
        self.get_date_menu_keyboard.add(*calendar)
