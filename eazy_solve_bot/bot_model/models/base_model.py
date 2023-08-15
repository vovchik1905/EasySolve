from typing import Any
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

class BazeBotModel:
    
    def __init__(self, bot_token: str, bot_url: str, bot_name: str, bot_tg_link: str) -> None:
        self.storage = MemoryStorage()
        self.bot_token = bot_token
        self.bot_url = bot_url
        self.bot_name = bot_name
        self.bot_tg_link = bot_tg_link
        self.bot = Bot(token = bot_token)
        self.dp = Dispatcher(self.bot, storage = self.storage)

    
    @property
    def start(self) -> None:
        executor.start_polling(self.dp, skip_updates=False)

    @property
    def stop(self) -> None:
        pass
        #self.dp.stop_polling()