from .attack_type import AttackType
import random

class Move:
    def __init__(self, name, power, accuracy, attack_type):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.attack_type = attack_type

    def execute(self):
        hit_chance = random.random()
        if hit_chance <= self.accuracy:
            print(f"{self.name} acertou!")
            return True
        else:
            print(f"{self.name} errou!")
            return False
    
    def __str__(self):

        return f"{self.name} (Type: {self.attack_type.value}, Power: {self.power}, Accuracy: {self.accuracy})"
