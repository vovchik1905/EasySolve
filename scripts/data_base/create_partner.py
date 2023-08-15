from eazy_solve_bot.bot_model.app.db.requests.create_db import CreateDataBase, db
from eazy_solve_bot.settings.general.general_settings import GeneralSettings


def main():
    easy_solve_data_base = CreateDataBase(db)
    easy_solve_data_base.create_partner(GeneralSettings.PARTNER_SETTINGS["telegram"],
                                        GeneralSettings.PARTNER_SETTINGS["language"],
                                        GeneralSettings.PARTNER_SETTINGS["currency"],
                                        GeneralSettings.PARTNER_SETTINGS["payment_info"],
                                        GeneralSettings.PARTNER_SETTINGS["privileges"],
                                        GeneralSettings.PARTNER_SETTINGS["client_status"],
                                        GeneralSettings.PARTNER_SETTINGS["solver"],
                                        GeneralSettings.PARTNER_SETTINGS["solver_status"])

if __name__ == "__main__":
    main()