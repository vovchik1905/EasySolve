from settings.private.bot_config.bot_config import PrivateBotSettings
from bot_model.models.main_model import MainBotModel


def EazySolveBot():
    eazy_solve_bot = MainBotModel(PrivateBotSettings.BOT_TOKEN, PrivateBotSettings.BOT_URL,
                                PrivateBotSettings.BOT_NAME, PrivateBotSettings.BOT_TG_LINK)
    eazy_solve_bot.action
    eazy_solve_bot.start