from abc import ABC, abstractproperty, abstractclassmethod, abstractstaticmethod, abstractmethod
from typing import Any
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from bot_model.app.step_models.commands.bot_commands import BotCommand
from bot_model.app.step_models.step_model import StepModel
from aiogram.dispatcher.filters.state import State

class CommandModel(StepModel):
    """
    """
    @abstractmethod
    def __init__(self, bot: Bot, dp: Dispatcher, command: BotCommand, state: State = None) -> None:
        super().__init__(bot, dp, state)
        self.command = command
    
    @abstractmethod
    async def logic(self, data: Any) -> State:
        return super().logic(data)
    
    @abstractmethod
    async def db(self, next_state: State, data: Any) -> Any:
        return super().db(next_state, data)
    
    @abstractmethod
    def view(self) -> None:
        return super().view()
    
    @abstractproperty
    def action(self):
        return super().action