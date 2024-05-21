from abc import ABC, abstractmethod

class BattleState(ABC):
    @abstractmethod
    def execute(self, battle):
        pass