from .pokemon_type import PokemonType
from .attack_type import AttackType

class TypeEffectiveness:
    effectiveness_chart = {
        AttackType.WATER: {
            PokemonType.FIRE: 2.0,
            PokemonType.WATER: 0.5,
            PokemonType.GRASS: 0.5,
            PokemonType.ELECTRIC: 1.0,
        },
        AttackType.FIRE: {
            PokemonType.FIRE: 0.5,
            PokemonType.WATER: 0.5,
            PokemonType.GRASS: 2.0,
            PokemonType.ELECTRIC: 1.0,
        },
        AttackType.GRASS: {
            PokemonType.FIRE: 0.5,
            PokemonType.WATER: 2.0,
            PokemonType.GRASS: 0.5,
            PokemonType.ELECTRIC: 1.0,
        },
        AttackType.ELECTRIC: {
            PokemonType.FIRE: 1.0,
            PokemonType.WATER: 2.0,
            PokemonType.GRASS: 0.5,
            PokemonType.ELECTRIC: 0.5,
        },
        AttackType.NORMAL: {
            PokemonType.FIRE: 1.0,
            PokemonType.WATER: 1.0,
            PokemonType.GRASS: 1.0,
            PokemonType.ELECTRIC: 1.0,
        }
    }

    @classmethod
    def get_effectiveness(cls, attack_type, defender_type):
        return cls.effectiveness_chart.get(attack_type, {}).get(defender_type, 1.0)
