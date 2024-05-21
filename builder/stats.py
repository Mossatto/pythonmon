class PokemonStats:
    def __init__(self, attack, defense, hp):
        self.attack = attack
        self.defense = defense
        self.hp = hp

    def __str__(self):
        return f"Ataque: {self.attack}, Defesa: {self.defense}, HP: {self.hp}"
