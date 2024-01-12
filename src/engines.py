import random
from enums import GameAction
from abc import ABCMeta, abstractmethod

Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}

class ActionEngine(metaclass=ABCMeta):

    def __init__(self):
        self._opponent_history = []

    @abstractmethod
    def generate_action(self):
        pass

    def action_message(self, action):
        print(f"Computer picked {action.name}.")

    def add_opponent_action(self, action):
        self._opponent_history.append(action)