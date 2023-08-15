from abc import ABC, abstractproperty, abstractclassmethod, abstractstaticmethod, abstractmethod
from typing import Any
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State

class StepModel(ABC):
    """
    """
    @abstractmethod
    def __init__(self, bot: Bot, dp: Dispatcher, state: State) -> None:
        self.bot = bot
        self.dp = dp
        self.state = state

    @abstractmethod
    async def logic(self, data: Any) -> State:
        pass

    @abstractmethod
    async def db(self, next_state: State, data: Any) -> Any:
        pass

    @abstractmethod
    def view(self) -> None:
        pass

    @abstractproperty
    def action(self):
        pass