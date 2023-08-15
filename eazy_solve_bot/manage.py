from bot_model.app.db.requests.create_db import CreateDataBase, db
from settings.general.general_settings import GeneralSettings

def main():
    easy_solve_data_base = CreateDataBase(db)
    easy_solve_data_base.create_db
    easy_solve_data_base.setting_up_all_tables
    easy_solve_data_base.create_partner(GeneralSettings.CREATOR_SETTINGS["telegram"],
                                        GeneralSettings.CREATOR_SETTINGS["language"],
                                        GeneralSettings.CREATOR_SETTINGS["currency"],
                                        GeneralSettings.CREATOR_SETTINGS["payment_info"],
                                        GeneralSettings.CREATOR_SETTINGS["privileges"],
                                        GeneralSettings.CREATOR_SETTINGS["client_status"],
                                        GeneralSettings.CREATOR_SETTINGS["solver"],
                                        GeneralSettings.CREATOR_SETTINGS["solver_status"])
    
    easy_solve_data_base.create_partner(GeneralSettings.PARTNER_SETTINGS["telegram"],
                                        GeneralSettings.PARTNER_SETTINGS["language"],
                                        GeneralSettings.PARTNER_SETTINGS["currency"],
                                        GeneralSettings.PARTNER_SETTINGS["payment_info"],
                                        GeneralSettings.PARTNER_SETTINGS["privileges"],
                                        GeneralSettings.PARTNER_SETTINGS["client_status"],
                                        GeneralSettings.PARTNER_SETTINGS["solver"],
                                        GeneralSettings.PARTNER_SETTINGS["solver_status"])
    
    easy_solve_data_base.create_partner_source(GeneralSettings.MAIN_SOURCE_SETTINGS["tg_id"],
                                                GeneralSettings.MAIN_SOURCE_SETTINGS["url"],
                                                GeneralSettings.MAIN_SOURCE_SETTINGS["name"],
                                                GeneralSettings.MAIN_SOURCE_SETTINGS["country"])


if __name__ == "__main__":
    main()
#____________-----------------------------------___________________________-__-------------------------------------------


#def main():
#    easy_solve_data_base = CreateDataBase(db)
#    easy_solve_data_base.create_partner(GeneralSettings.PARTNER_SETTINGS["telegram"],
#                                        GeneralSettings.PARTNER_SETTINGS["language"],
#                                        GeneralSettings.PARTNER_SETTINGS["currency"],
#                                        GeneralSettings.PARTNER_SETTINGS["payment_info"],
#                                        GeneralSettings.PARTNER_SETTINGS["privileges"],
#                                        GeneralSettings.PARTNER_SETTINGS["client_status"],
#                                        GeneralSettings.PARTNER_SETTINGS["solver"],
#                                        GeneralSettings.PARTNER_SETTINGS["solver_status"])
#
#if __name__ == "__main__":
#    main()
###________________---------------------------------------------------------____________________
#
#from bot_model.app.db.requests.create_db import CreateDataBase, db
#from settings.general.general_settings import GeneralSettings
#
#
#def main():
#    easy_solve_data_base = CreateDataBase(db)
#    easy_solve_data_base.create_partner_source(GeneralSettings.MAIN_SOURCE_SETTINGS["tg_id"],
#                                                GeneralSettings.MAIN_SOURCE_SETTINGS["url"],
#                                                GeneralSettings.MAIN_SOURCE_SETTINGS["name"],
#                                                GeneralSettings.MAIN_SOURCE_SETTINGS["country"])
#    
#
#if __name__ == "__main__":
#    main()
#
##from bot_model.app.db.requests.create_db import CreateDataBase, db
#from settings.general.general_settings import GeneralSettings
#from bot_model.app.db.db_model.db_model import *
#
#
#def main():
#    with db:
#        user_privileges = User.select(User.id).where(User.id == 1).get().id
#        print(user_privileges)
#    
#
#if __name__ == "__main__":
#    main()