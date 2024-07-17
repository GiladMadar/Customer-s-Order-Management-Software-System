from overrides import overrides
from animal import Animal, Pet


class Fish(Animal, Pet):
    def __init__(self, name: str, legs=0):
        self.name = name
        self.legs = legs

    @overrides
    def setName(self, name):
        self.name = name

    @overrides
    def getName(self):
        return self.name

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
        return f"Fish name: {self.name}"
