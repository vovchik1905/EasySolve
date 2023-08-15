from eazy_solve_bot.bot_model.app.db.requests.create_db import CreateDataBase, db


def main():
    easy_solve_data_base = CreateDataBase(db)
    easy_solve_data_base.setting_up_all_tables

if __name__ == "__main__":
    main()