from animals.animal import Animal
from animals.pet import Pet
from overrides import overrides

class Fish(Animal, Pet):
    def __init__(self, fish_name: str, legs=0):
        self.fish_name = fish_name

    @overrides
    def setName(self, fish_name):
        self.fish_name = fish_name

    @overrides
    def getName(self):
        return self.fish_name

    @overrides
    def eat(self):
        print("The Fish is eating now!")

    @overrides
    def play(self):
        print("The Fish is playing now!")

    @overrides
    def walk(self):
        print("The Fish is swimming now!")

    def __str__(self):
        return f"Fish name: {self.fish_name}"
