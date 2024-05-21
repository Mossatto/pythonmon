from .pokemon import Pokemon
from .move import *
from .pokemon_type import *
from .stats import PokemonStats

class PokemonBuilder:
    def __init__(self):
        self.name = None
        self.type = None
        self.moves = []

    def set_name(self, name):
        self.name = name
        return self

    def set_type(self, pokemon_type):
        if not isinstance(pokemon_type, PokemonType):
            raise ValueError(f"pokemon_type deve ser uma instância de PokemonType, mas recebeu {type(pokemon_type).__name__}")
        self.type = pokemon_type
        return self
    
    def set_stats(self, attack, defense, hp):
        self.stats = PokemonStats(attack, defense, hp)
        return self

    def add_move(self, move):
        if not isinstance(move, Move):
            raise ValueError(f"move deve ser uma instância de Move, mas recebeu {type(move).__name__}")
        if len(self.moves) >= 4:
            raise ValueError("Um Pokémon não pode ter mais de 4 ataques")
        self.moves.append(move)
        return self

    def build(self):
        if self.name is None or self.type is None or self.stats is None:
            raise ValueError("Os atributos name, type e stats devem ser definidos antes de construir o objeto Pokemon")
        return Pokemon(self.name, self.type, self.stats, self.moves)