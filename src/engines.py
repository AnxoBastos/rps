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

class RandomEngine(ActionEngine):
    
    def __init__(self):
        super().__init__()

    def generate_action(self):
            computer_selection = random.randint(0, len(GameAction) - 1)
            computer_action = GameAction(computer_selection)
            return computer_action

class TenMovesEngine(ActionEngine):
    
    def __init__(self):
        super().__init__()

    def generate_action(self):
        last_ten = self._opponent_history[-10:]
        most_frequent = max(set(last_ten), default=None, key=last_ten.count)

        if most_frequent == None:
            most_frequent = GameAction.Rock

        return Victories[most_frequent]