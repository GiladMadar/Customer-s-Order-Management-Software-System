from overrides import overrides
from animal import Animal, Pet


class Spider(Animal, Pet):
    def __init__(self, name: str, legs=8):
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
        print(f"{self.name} the Spider is playing!")

    @overrides
    def eat(self):
        print("The Spider is eating now!")

    @overrides
    def walk(self):
        print("The Spider is walking now!")

    def __str__(self):
        return f"Spider name: {self.name}"
