from items.consumables import HealingItem
from items.stat_boosters import StatBooster
from items.promotion_items import PromotionItem

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
    
    @staticmethod
    def concoction():
        return HealingItem(
            name="Concoction",
            description="Restores 20 HP",
            heal_amount=20,
            uses=2
        )
    
    @staticmethod
    def elixir():
        return HealingItem(
            name="Elixir",
            description="Fully restores HP",
            heal_amount=999,
            uses=1
        )
    
    # ======================
    # STAT BOOSTERS
    # ======================

    @staticmethod
    def energy_drop():
        return StatBooster(
            name="Energy Drop",
            description="Permanently increases Strength",
            stat="str",
            amount=2
        )

    @staticmethod
    def speedwing():
        return StatBooster(
            name="Speedwing",
            description="Permanently increases Speed",
            stat="spd",
            amount=2
        )

    @staticmethod
    def secret_book():
        return StatBooster(
            name="Secret Book",
            description="Permanently increases Skill",
            stat="skl",
            amount=2
        )

    @staticmethod
    def goddess_icon():
        return StatBooster(
            name="Goddess Icon",
            description="Permanently increases Luck",
            stat="lck",
            amount=2
        )

    @staticmethod
    def dracoshield():
        return StatBooster(
            name="Dracoshield",
            description="Permanently increases Defense",
            stat="def_",
            amount=2
        )

    @staticmethod
    def talisman():
        return StatBooster(
            name="Talisman",
            description="Permanently increases Resistance",
            stat="res",
            amount=2
        )

    @staticmethod
    def boots():
        return StatBooster(
            name="Boots",
            description="Permanently increases Movement",
            stat="mov",
            amount=1
        )
