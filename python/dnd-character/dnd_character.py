import numpy as np
def modifier(value):
    value -= 10
    return int(np.floor(float(value)/2))

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10+modifier(self.constitution)

    def ability(self):
        return sum(sorted(np.random.randint(low=1, high=7,size=4))[1:])
