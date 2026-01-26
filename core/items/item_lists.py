from items.consumables import HealingItem
from items.stat_boosters import StatBooster

class ItemRegistry:
    @staticmethod
    def vulnerary():
        return HealingItem(
            name="Vulnerary",
            description="Restores 10 HP",
            heal_amount=10,
            uses=3
        )

    @staticmethod
    def energy_drop():
        return StatBooster(
            name="Energy Drop",
            description="Permanently increases Strength",
            stat="str",
            amount=2
        )
