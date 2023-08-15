from aiogram.dispatcher.filters.state import State, StatesGroup


class BotStates(StatesGroup):
    CHECKING_USER_SUBSCRIPTION_STEP = State()   #1
    CLIENT_MAIN_MENU = State()                  #1
    CLIENT_AND_SOLVER_MAIN_MENU = State()       #1
    PARTNER_MAIN_MENU = State()                 #1
    ADMIN_MAIN_MENU = State()                   #1
    ACCOUNTANT_MAIN_MENU = State()              #1
    CREATOR_MAIN_MENU = State()                 #1

    PARTNER_CONTROL_MENU = State()
    ADMIN_CONTROL_MENU = State()
    ACCOUNTANT_CONTROL_MENU = State()
    CREATOR_CONTROL_MENU = State()

    SETTING_UP_USER_LANGUAGE = State()          #2
    SETTING_UP_USER_TIME_ZONE = State()         #2
    NEW_ORDER_STEP = State()                    #2
    ACTIVE_ORDERS_STEP = State()                #2
    MY_PROFILE_STEP = State()                   #2
    BALANCE_STEP = State()                      #2
    SUPPORT_STEP = State()                      #2
    REVIEWS_STEP = State()                      #2
    AFFILIATE_PROGRAM_STEP = State()            #2
    SOLVER_MENU_STEP = State()                  #2

    #my profile menu
    SET_BANKING_DETAILS_STEP = State()
    SET_CURRENCY_STEP = State()
    SET_LANGUAGE_STEP = State()

    #balance menu
    CASH_IN_STEP = State()
    CASH_OUT_STEP = State()

    #support menu
    BECOME_A_PARTNER_STEP = State()             #3
    BECOME_A_SOLVER_STEP = State()              #3
    ASK_A_QUESTION_STEP = State()               #3
    FAQ_STEP = State()                          #3

    #affiliate program step
    LIST_AFFILIATE_LINKS_STEP = State()
    CREATE_AFFILIATE_LINK_STEP = State()
    AFFILIATE_PROGRAM_STATISTICS_STEP = State()

    #new order menu
    NEW_ORDER_BY_ADMIN_STEP = State()
    
    NEW_ORDER_BY_BOT_STEP = State()
    #GET_ORDER_IMPORTANCE_STEP = State()
    MAIN_STANDART_ORDER_MENU_STEP = State()
    MAIN_NOW_ORDER_MENU_STEP = State()
    MAIN_IMPORTANT_ORDER_MENU_STEP = State()
    MAIN_VOLUMINOUS_ORDER_MENU_STEP = State()
    
    
    UNFINISHED_ORDER_STEP = State()

    #standart order menu
    GET_ORDER_IMPORTANCE = State()
    GET_ORDER_SUBJECT_STEP = State()
    GET_ORDER_TOPIC_STEP = State()
    GET_ORDER_COMMENT_STEP = State()
    GET_ORDER_FILES_STEP = State()
    GET_ORDER_DEADLINE_DATE_STEP = State()
    GET_ORDER_DEADLINE_TIME_STEP = State()
    GET_ORDER_NUMBER_OF_TASKS_STEP = State()
    GET_ORDER_DURATION_TIME_STEP = State()
    GET_UP_ORDER_SETTINGS_STEP = State()
    
    GET_ORDER_FORMAT_STEP = State()
    
    GET_ORDER_SUPPORT_DATE_STEP = State()
    GET_ORDER_SUPPORT_TIME_STEP = State()
    GET_ORDER_SUPPORT_COMMENT_STEP = State()

    GET_ORDER_PREFERRED_BUDGET_STEP = State()
    
    GET_ORDER_PERCENT_COMPLET_STEP = State()
    
    SEND_ORDER_TO_SOLVERS_STEP = State()