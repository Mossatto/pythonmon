from .choosing_move_state import ChoosingMoveState

class CheckVictoryState:
    def execute(self, battle):
        if battle.opponent_pokemon.current_hp <= 0:
            print(f"{battle.opponent_pokemon.name} fainted! {battle.current_pokemon.name} wins!")
        else:
            battle.switch_turns()
            battle.set_state(ChoosingMoveState())
