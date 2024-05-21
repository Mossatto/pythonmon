from .pokemon_type import PokemonType
from .attack_type import AttackType
from .type_effectiviness import TypeEffectiveness
from .stats import PokemonStats

class Pokemon:
    def __init__(self, name, pokemon_type, stats, moves=None):
        self.name = name
        self.type = pokemon_type
        self.stats = stats
        self.moves = moves if moves is not None else []
        self.current_hp = stats.hp

    def take_damage(self, damage):
        self.current_hp -= damage
        self.current_hp = max(self.current_hp, 0)  # HP não pode ser menor que 0
        print(f"{self.name} sofreu {damage} de dano. HP atual: {self.current_hp}/{self.stats.hp}")


    def __str__(self):
        moves_str = ", ".join(str(move) for move in self.moves)
        return f"Nome: {self.name}, Tipo: {self.type.value}, Ataques: {moves_str}"