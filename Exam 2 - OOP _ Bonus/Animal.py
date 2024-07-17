from abc import ABC, abstractmethod

# Abstract base classes
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def walk(self):
        pass


