from .move import Move
from .attack_type import AttackType
from .pokemon import Pokemon
from .pokemon_type import PokemonType

class MoveBuilder:
    def __init__(self):
        self.name = None
        self.power = None
        self.accuracy = None
        self.attack_type = None

    def set_name(self, name):
        self.name = name
        return self

    def set_power(self, power):
        self.power = power
        return self

    def set_accuracy(self, accuracy):
        self.accuracy = accuracy
        return self

    def set_attack_type(self, attack_type):
        if not isinstance(attack_type, AttackType):
            raise ValueError(f"attack_type deve ser uma instância de AttackType, mas recebeu {type(attack_type).__name__}")
        self.attack_type = attack_type
        return self

    def build(self):
        if self.name is None or self.power is None or self.accuracy is None or self.attack_type is None:
            raise ValueError("Todos os atributos devem ser definidos antes de construir o objeto Move")
        return Move(self.name, self.power, self.accuracy, self.attack_type)
