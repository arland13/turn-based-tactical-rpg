from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, description, consumable=True):
        self.name = name
        self.description = description
        self.consumable = consumable

    @abstractmethod
    def use(self, target):
        pass
