from .pokemon_type import PokemonType
from .attack_type import AttackType

class PokemonMoveManager:
    def __init__(self, pokemon):
        self.pokemon = pokemon
    @staticmethod
    def is_valid_move(pokemon, move):
        type_move_map = {
            PokemonType.WATER: [AttackType.WATER, AttackType.NORMAL],
            PokemonType.FIRE: [AttackType.FIRE, AttackType.NORMAL],
            PokemonType.GRASS: [AttackType.GRASS, AttackType.NORMAL],
            PokemonType.ELECTRIC: [AttackType.ELECTRIC, AttackType.NORMAL],
        }
        allowed_types = type_move_map.get(pokemon.type, [])
        return move.attack_type in allowed_types
    
    @staticmethod
    def add_or_replace_move(pokemon, move):
        
        if not PokemonMoveManager.is_valid_move(pokemon,move):
            print(f"{pokemon.name} não pode aprender {move.name} do tipo {move.attack_type.value}")
            return

        if len(pokemon.moves) < 4:
            pokemon.moves.append(move)
        else:
            print("Número máximo de ataques já aprendido.")
            choice = input("Você quer substituir um ataque? (sim/não): ")
            if choice.lower() == "sim":
                pokemon.show_moves()
                move_index = int(input("Digite o índice do ataque a ser substituído: "))
                if 0 <= move_index < len(pokemon.moves):
                    pokemon.moves[move_index] = move
                    print("Ataque substituído com sucesso.")
                else:
                    print("Índice de ataque inválido.")
            else:
                print("Novo ataque não adicionado.")

    def show_moves(self):
        print("Ataques atuais:")
        for i, move in enumerate(self.pokemon.moves):
            print(f"{i}: {move}")
