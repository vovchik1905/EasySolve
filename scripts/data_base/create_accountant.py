from eazy_solve_bot.bot_model.app.db.requests.create_db import CreateDataBase, db
from eazy_solve_bot.settings.general.general_settings import GeneralSettings


def main():
    easy_solve_data_base = CreateDataBase(db)
    easy_solve_data_base.create_partner(GeneralSettings.ACCOUNTANT_SETTINGS["telegram"],
                                        GeneralSettings.ACCOUNTANT_SETTINGS["language"],
                                        GeneralSettings.ACCOUNTANT_SETTINGS["currency"],
                                        GeneralSettings.ACCOUNTANT_SETTINGS["payment_info"],
                                        GeneralSettings.ACCOUNTANT_SETTINGS["privileges"],
                                        GeneralSettings.ACCOUNTANT_SETTINGS["client_status"],
                                        GeneralSettings.ACCOUNTANT_SETTINGS["solver"],
                                        GeneralSettings.ACCOUNTANT_SETTINGS["solver_status"])

if __name__ == "__main__":
    main()