from .choosing_move_state import ChoosingMoveState
from .attack_state import AttackState

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.current_pokemon = pokemon1
        self.opponent_pokemon = pokemon2
        self.state = ChoosingMoveState()

    def set_state(self, state):
        self.state = state

    def switch_turns(self):
        self.current_pokemon, self.opponent_pokemon = self.opponent_pokemon, self.current_pokemon

    def execute(self):
        while self.pokemon1.current_hp > 0 and self.pokemon2.current_hp > 0:
            self.state.execute(self)

        if self.pokemon1.current_hp <= 0:
            print(f"{self.pokemon1.name} fainted! {self.pokemon2.name} wins!")
        elif self.pokemon2.current_hp <= 0:
            print(f"{self.pokemon2.name} fainted! {self.pokemon1.name} wins!")
