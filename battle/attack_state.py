from .battle_state import BattleState
from builder.damage_dinamic import Battle

class AttackState(BattleState):
    def __init__(self, move):
        self.move = move

    def execute(self, battle):
        from .check_victory_state import CheckVictoryState
        if self.move.execute():
            damage = Battle.calculate_damage(battle.current_pokemon, self.move, battle.opponent_pokemon)
            battle.opponent_pokemon.take_damage(damage)
        battle.set_state(CheckVictoryState())
