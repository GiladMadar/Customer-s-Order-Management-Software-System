from overrides import overrides
from animal import Animal, Pet


class Cat(Animal, Pet):
    def __init__(self, name: str, legs=4):
        self.name = name
        self.legs = legs

    @overrides
    def setName(self, name):
        self.name = name

    @overrides
    def getName(self):
        return self.name

    @overrides
    def play(self):
        print("The Cat is playing now!")

    @overrides
    def eat(self):
        print("The Cat is eating now!")

    @overrides
    def walk(self):
        print("The Cat is walking now!")

    def __str__(self):
        return f"Cat name: {self.name}"
