from eazy_solve_bot.bot_model.app.db.requests.create_db import CreateDataBase, db
from eazy_solve_bot.settings.general.general_settings import GeneralSettings


def main():
    easy_solve_data_base = CreateDataBase(db)
    easy_solve_data_base.create_partner_source(GeneralSettings.MAIN_SOURCE_SETTINGS["tg_id"],
                                                GeneralSettings.MAIN_SOURCE_SETTINGS["url"],
                                                GeneralSettings.MAIN_SOURCE_SETTINGS["name"],
                                                GeneralSettings.MAIN_SOURCE_SETTINGS["country"])
    

if __name__ == "__main__":
    main()