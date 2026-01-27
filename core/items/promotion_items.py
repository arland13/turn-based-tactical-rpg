from items.item import Item
from entities.promotion import PromotionError

class MasterSeal(Item):
    def __init__(self):
        super().__init__(
            name="Master Seal",
            description="Promotes an unpromoted unit",
            consumable=True
        )

    def use(self, target):
        if not target.can_promote():
            raise PromotionError("Unit is not ready to promote")

        target.promote_from_table()
        return True


class MasterCrown(Item):
    def __init__(self):
        super().__init__(
            name="Master Crown",
            description="Promotes a unit regardless of level",
            consumable=True
        )

    def use(self, target):
        if not target.can_promote(ignore_level=True):
            raise PromotionError("Cannot promote this unit")

        target.promote_from_table(ignore_level=True)
        return True
    
class HolyCrown():
    def __init__(self):
        super().__init__(
            name="Holy Crown",
            description="Doubles unit stat growths",
            consumable=False
        )

    def use(self, target):
        for stat in target.GROWTHS:
            target.GROWTHS[stat] = min(100, target.GROWTHS[stat] * 2)
            target.has_holy_crown = True

        print(f"✨ {target.name}'s growth rates doubled!")
        return False
