from animals.animal import Animal
from animals.pet import Pet
from overrides import overrides

class Spider(Pet, Animal):
    def __init__(self, name: str, legs=8):
        self.name = name

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
