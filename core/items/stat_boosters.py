from items.item import Item

class StatBooster(Item):
    def __init__(self, name, description, stat, amount):
        super().__init__(name, description, consumable=True)
        self.stat = stat
        self.amount = amount

    def use(self, target):
        if not hasattr(target, self.stat):
            raise ValueError(f"{target.name} has no stat {self.stat}")

        setattr(target, self.stat, getattr(target, self.stat) + self.amount)
        print(f"{target.name}'s {self.stat.upper()} increased by {self.amount} permanently!")
        return True
