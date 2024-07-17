from abc import ABC, abstractmethod

class Gift(ABC):
    @abstractmethod
    def open_gift(self):
        pass

class ConcreteGift(Gift):
    def open_gift(self):
        print("Congratulations! You got a new gift! Enjoy!")

# Additional concrete gift types can be defined similarly
