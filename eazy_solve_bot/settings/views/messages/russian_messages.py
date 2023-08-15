from settings.private.channel_config.channel_config import ChannelConfig
from settings.private.finance.finance import FinanceSettings
from settings.private.admin_config.admin_config import AdminConfig
from settings.general.general_settings import GeneralSettings


class RussianMessages:
    #special
    MAIN_MENU_MESSAGE = "Главное меню."
    BAD_USER_ANSWER_MESSAGE = "Нет такого варианта ответа."
    #commands
    START_COMMAND_MESSAGE = "START_MSG"
    HELP_COMMAND_MESSAGE = "HELP_COMMAND"
    MAIN_MENU_COMMAND_MESSAGE = "MAIN_MENU_COMMAND"

    CHECKING_USER_SUBSCRIPTION_MESSAGE = f"Для работы с ботом пожалуйста подпишитесь на наш канал.\nTo work with the bot, please subscribe to our channel.\n{ChannelConfig.CHANNEL_URL}"
    SETTING_UP_USER_LANGUAGE_MESSAGE = "Пожалуйста задайте свой язык.\nPlease specify your language."
    RESETTING_UP_USER_LANGUAGE_STEP = "К сожалению данный язык пока не поддерживается. Воспользуйтесь другим языком.\nUnfortunately, this language is not supported yet. Use a different language."
    SETTING_UP_USER_TIME_ZONE_MESSAGE = "Задайте свой часовой пояс в формате: UTC."
    CLIENT_MAIN_MENU_MESSAGE = "CLIENT_MAIN_MENU_MESSAGE"
    CLIENT_AND_SOLVER_MAIN_MENU_MESSAGE = "CLIENT_AND_SOLVER_MAIN_MENU_MESSAGE"
    PARTNER_MAIN_MENU_MESSAGE = "PARTNER_MAIN_MENU_MESSAGE"
    ADMIN_MAIN_MENU_MESSAGE = "ADMIN_MAIN_MENU_MESSAGE"
    ACCOUNTANT_MAIN_MENU_MESSAGE = "ACCOUNTANT_MAIN_MENU_MESSAGE"
    CREATOR_MAIN_MENU_MESSAGE = "CREATOR_MAIN_MENU_MESSAGE"

    PARTNER_CONTROL_MENU_MESSAGE = "PARTNER_CONTROL_MENU"
    ADMIN_CONTROL_MENU_MESSAGE = "ADMIN_CONTROL_MENU"
    ACCOUNTANT_CONTROL_MENU_MESSAGE = "ACCOUNTANT_CONTROL_MENU"
    CREATOR_CONTROL_MENU_MESSAGE = "CREATOR_CONTROL_MENU"

    NEW_ORDER_MESSAGE = "NEW_ORDER_MESSAGE"
    ACTIVE_ORDERS_MESSAGE = "ACTIVE_ORDERS_MESSAGE"
    MY_PROFILE_MESSAGE = "MY_PROFILE_MESSAGE"
    BALANCE_MESSAGE = "BALANCE_MESSAGE"
    SUPPORT_MESSAGE = "SUPPORT_MESSAGE"
    REVIEWS_MESSAGE = "REVIEWS_STEP"
    AFFILIATE_PROGRAM_MESSAGE = "AFFILIATE_PROGRAM"
    SOLVER_MENU_MESSAGE = "SOLVER_MENU_MESSAGE"
    #new order menu
    NEW_ORDER_BY_ADMIN_MESSAGE = f"Заказ через администратора стоит больше на {FinanceSettings.ORDER_BY_ADMIN_PRICE} рублей, чтобы сделать заказ напишите: {AdminConfig.ADMIN_TG_USERNAME}"
    NEW_ORDER_BY_BOT_MESSAGE = "Заказ через бота"
    UNFINISHED_ORDER_MESSAGE = "Не отправленные заказы"
    GET_ORDER_SETTINGS_MESSAGE = "Настройте параметры заказа"
    #
    GET_ORDER_SUBJECT_MESSAGE = "Выберите предмет"
    GET_ORDER_COMMENT_MESSAGE = "Напишите комментарий к заказу"
    GET_ORDER_FILES_MESSAGE = "Прикрепите файлы к заказу"
    GET_ORDER_DEADLINE_DATE_MESSAGE = "Задайте дату дэдлайна (Воспользуйтесь клавиатурой или ответьте сообщением в формате YYYY.MM.DD)"
    GET_ORDER_DEADLINE_TIME_MESSAGE = "Задайте время дэдлайна"
    GET_UP_ORDER_SETTINGS_MESSAGE = "Задайте дополнительные настройки"
    SEND_ORDER_TO_SOLVERS_MESSAGE = "Всё верно?"
    GET_ORDER_SUPPORT_DATE_MESSAGE = "Задайте дату дэдлайна поддержки (Воспользуйтесь клавиатурой или ответьте сообщением в формате YYYY.MM.DD)"
    GET_ORDER_SUPPORT_TIME_MESSAGE = "Задайте время дэдлайна поддержки заказа (воспользуйтесь клавиатурой/ сообщением в формате ЧЧ:ММ)"
    GET_ORDER_SUPPORT_COMMENT_MESSAGE = "Задайте комментарий по поддержке заказа"
    GET_ORDER_PERCENT_COMPLET_MESSAGE = "Задайте минимально необходимый процент выполнения работы, в случае если работа не будет выполнена на этот процент вернём вам полную стоимость заказа."
    GET_ORDER_PREFERRED_BUDGET_MESSAGE = "Задайте предпочитаемый бюджет заказа."
    GET_ORDER_FORMAT_MESSAGE = "Выберите тип работы."
    GET_ORDER_NUMBER_OF_TASKS_MESSAGE = "Задайте количество задач в работе"
    GET_ORDER_DURATION_TIME_MESSAGE = "Задайте оставшееся время работы"
    #
    GET_ORDER_TOPIC_MESSAGE = "Выберите тему"
    #get order file messages
    ORDER_FILE_ADDED_MESSAGE = "Файл добавлен!"
    ORDER_INVALID_FILE_MESSAGE = "Недопустимый файл!"
    EXCEEDED_THE_ALLOWED_LIMIT_OF_ORDER_FILES_MESSAGE = f"Превышен допустимый лимит в {GeneralSettings.ORDER_FILES_QUANTITY_LIMIT} файлов!"
    DELETE_ALL_ORDER_FILES_MESSAGE = "Все файлы удалены!"
    #my profile menu
    SET_BANKING_DETAILS_MESSAGE = "SET_BANKING_DETAILS_MESSAGE"
    SET_CURRENCY_MESSAGE = "SET_CURRENCY_MESSAGE"
    SET_LANGUAGE_MESSAGE = "SET_LANGUAGE_MESSAGE"
    #balance menu
    CASH_IN_MESSAGES = "CASH_IN_MESSAGES"
    CASH_OUT_MESSAGES = "CASH_OUT_MESSAGES"
    #support menu
    BECOME_A_PARTNER_MESSAGE = "BECOME_A_PARTNER_MESSAGE"
    BECOME_A_SOLVER_MESSAGE = "BECOME_A_SOLVER_MESSAGE"
    ASK_A_QUESTION_MESSAGE = "ASK_A_QUESTION_MESSAGE"
    FAQ_MESSAGE = "FAQ_MESSAGE"
    #affiliate program menu
    LIST_AFFILIATE_LINKS_MESSAGE = "LIST_AFFILIATE_LINKS_MESSAGE"
    CREATE_AFFILIATE_LINK_MESSAGE = "CREATE_AFFILIATE_LINK_MESSAGE"
    AFFILIATE_PROGRAM_STATISTICS_MESSAGE = "AFFILIATE_PROGRAM_STATISTICS_MESSAGE"