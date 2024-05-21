from .type_effectiviness import TypeEffectiveness
import random
from .stats import *

class Battle:
    @staticmethod
    def calculate_damage(attacking_pokemon, move, defending_pokemon):
        effectiveness = TypeEffectiveness.get_effectiveness(move.attack_type, defending_pokemon.type)
        modifier = Battle.calculate_modifier(effectiveness)
        base_damage = Battle.calculate_base_damage(attacking_pokemon, move, defending_pokemon)
        damage = Battle.apply_modifier(base_damage, modifier)
        return damage
    
    def execute_move(attacker, move, defender):
        hit_chance = random.random()
        if hit_chance <= move.accuracy / 100:
            print(f"{move.name} acertou!")
            damage = Battle.calculate_damage(attacker, move, defender)
            Battle.apply_damage(defender, damage)
        else:
            print(f"{move.name} errou!")
    
    @staticmethod
    def calculate_modifier(effectiveness):
        # Lógica para calcular o modificador de dano com base na efetividade
        # Exemplo simplificado:
        if effectiveness == 2:
            return 2  # Ataque super efetivo
        elif effectiveness == 0.5:
            return 0.5  # Ataque pouco efetivo
        else:
            return 1  # Ataque neutro

    @staticmethod
    def calculate_base_damage(attacking_pokemon, move, defending_pokemon):
        # Lógica para calcular o dano base do ataque
        base_damage = (8 * attacking_pokemon.stats.attack / defending_pokemon.stats.defense) * move.power / 50 + 2
        return base_damage

    @staticmethod
    def apply_modifier(damage, modifier):
        # Lógica para aplicar o modificador de dano ao dano base
        return damage * modifier

    @staticmethod
    def apply_damage(defending_pokemon, damage):
        defending_pokemon.current_hp -= damage
        if defending_pokemon.current_hp <= 0:
            defending_pokemon.current_hp = 0
            print(f"{defending_pokemon.name} desmaiou!")
