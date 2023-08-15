from eazy_solve_bot.bot_model.app.db.requests.create_db import CreateDataBase, db
from eazy_solve_bot.settings.general.general_settings import GeneralSettings


def main():
    easy_solve_data_base = CreateDataBase(db)
    easy_solve_data_base.create_partner(GeneralSettings.ADMIN_SETTINGS["telegram"],
                                        GeneralSettings.ADMIN_SETTINGS["language"],
                                        GeneralSettings.ADMIN_SETTINGS["currency"],
                                        GeneralSettings.ADMIN_SETTINGS["payment_info"],
                                        GeneralSettings.ADMIN_SETTINGS["privileges"],
                                        GeneralSettings.ADMIN_SETTINGS["client_status"],
                                        GeneralSettings.ADMIN_SETTINGS["solver"],
                                        GeneralSettings.ADMIN_SETTINGS["solver_status"])

if __name__ == "__main__":
    main()