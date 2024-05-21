from builder import *
from battle.battle import Battle


def main():
    # Criar movimentos
    move1 = MoveBuilder().set_name("Water Gun").set_power(40).set_accuracy(1.0).set_attack_type(AttackType.WATER).build()
    move2 = MoveBuilder().set_name("Tackle").set_power(40).set_accuracy(1.0).set_attack_type(AttackType.NORMAL).build()
    move3 = MoveBuilder().set_name("Flamethrower").set_power(90).set_accuracy(1.0).set_attack_type(AttackType.FIRE).build()
    move4 = MoveBuilder().set_name("Thunder Shock").set_power(40).set_accuracy(1.0).set_attack_type(AttackType.ELECTRIC).build()

    # Criar Pokemons
    squirtle = (PokemonBuilder()
                .set_name("Squirtle")
                .set_type(PokemonType.WATER)
                .set_stats(attack=48, defense=65, hp=44)
                .add_move(move1)
                .add_move(move2)
                .build())

    charmander = (PokemonBuilder()
                  .set_name("Charmander")
                  .set_type(PokemonType.FIRE)
                  .set_stats(attack=52, defense=43, hp=39)
                  .add_move(move3)
                  .add_move(move2)
                  .build())

    # Iniciar batalha
    battle = Battle(squirtle, charmander)
    battle.execute()

if __name__ == "__main__":
    main()