from items.item import Item

class HealingItem(Item):
    def __init__(self, name, description, heal_amount, uses=3):
        super().__init__(name, description, consumable=True)
        self.heal_amount = heal_amount
        self.uses = uses

    def use(self, target):
        if self.uses <= 0:
            raise ValueError("No uses left")

        healed = min(self.heal_amount, target.hp_max - target.hp)
        target.hp += healed
        self.uses -= 1

        print(f"{target.name} recovered {healed} HP")

        return self.uses == 0
