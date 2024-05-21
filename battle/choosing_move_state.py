from .battle_state import BattleState
from .attack_state import AttackState


class ChoosingMoveState(BattleState):
    def execute(self, battle):
        print(f"{battle.current_pokemon.name}'s Turn! Choose a move:")
        for i, move in enumerate(battle.current_pokemon.moves):
            print(f"{i}. {move}")

        move_index = int(input("Enter the move number: "))
        chosen_move = battle.current_pokemon.moves[move_index]
        battle.set_state(AttackState(chosen_move))