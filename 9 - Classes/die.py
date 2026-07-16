from random import randint

class Die():
    "Simple representation of a die"
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        "It simulates the rolling of a die returning a random number of side"
        return randint(1, self.sides)
    
die = Die()
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())