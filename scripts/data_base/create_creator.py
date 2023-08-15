from eazy_solve_bot.bot_model.app.db.requests.create_db import CreateDataBase, db
from eazy_solve_bot.settings.general.general_settings import GeneralSettings


def main():
    easy_solve_data_base = CreateDataBase(db)
    easy_solve_data_base.create_partner(GeneralSettings.CREATOR_SETTINGS["telegram"],
                                        GeneralSettings.CREATOR_SETTINGS["language"],
                                        GeneralSettings.CREATOR_SETTINGS["currency"],
                                        GeneralSettings.CREATOR_SETTINGS["payment_info"],
                                        GeneralSettings.CREATOR_SETTINGS["privileges"],
                                        GeneralSettings.CREATOR_SETTINGS["client_status"],
                                        GeneralSettings.CREATOR_SETTINGS["solver"],
                                        GeneralSettings.CREATOR_SETTINGS["solver_status"])

if __name__ == "__main__":
    main()