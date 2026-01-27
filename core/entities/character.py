from entities.promotion import PromotionError, PromotionData
import random

class Character:
    def __init__(
        self,
        name,
        symbol,
        faction,
        has_acted,
        hp,
        max_hp,
        str,
        mag,
        skl,
        spd,
        lck,
        def_,
        res,
        mov,
    ):
        self.name = name
        self.symbol = symbol
        self.faction = faction
        self.has_acted = has_acted
        self.hp = hp
        self.max_hp = max_hp
        self.str = str
        self.mag = mag
        self.skl = skl
        self.spd = spd
        self.lck = lck
        self.def_ = def_
        self.res = res
        self.mov = mov
        
        self.skills = []
        self.inventory = []
        self.weapon = None
        self.promoted = False
        self.base_class_name = self.__class__.__name__
        
    def show_stat(self):
        return (
            f"Name : {self.name}\t"f"Hp  : {self.hp}\n"
            f"Str  : {self.str}\t"f"Mag  : {self.mag}\n"
            f"Skl  : {self.skl}\t"f"Spd  : {self.spd}\n"
            f"Lck  : {self.lck}\t"f"Def  : {self.def_}\n"
            f"Res  : {self.res}\t"f"Mov  : {self.mov}"
            )
    
    def show_items(self):
        return self.inventory
    
    def level_up(self):
        self.level += 1
        for stat, growth in self.GROWTHS.items():
            if random.randint(1, 100) <= growth:
                setattr(self, stat, getattr(self, stat) + 1)
                if stat == "hp":
                    self.max_hp += 1
                    self.hp += 1

    def equip_skill(self, skill):
        self.skills.append(skill)
        
    def show_skills(self):
        return [skill.name for skill in self.skills]
    
    def equip_weapon(self, weapon):
        if weapon.weapon_type in self.ALLOWED_WEAPONS:
            self.weapon = weapon
        else:
            raise ValueError(
                f"{self.__class__.__name__} cannot equip {weapon.weapon_type.value}"
            )
            
    def add_item(self, item):
        if len(self.inventory) >= 5:
            raise ValueError("Inventory full")
        self.inventory.append(item)
        
    def use_item(self, item, target=None):
        target = target or self
        consumed = item.use(target)
        
        if consumed:
            self.inventory.remove(item)

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} gains {amount} EXP! (EXP: {self.exp}/{self.exp_to_next})")

        while self.exp >= self.exp_to_next:
            self.exp -= self.exp_to_next
            self.level_up()
            print(f"🎉 {self.name} leveled up! (Level {self.level})")

    def can_promote(self, ignore_level=False):
        if self.promoted:
            return False
        if ignore_level:
            return True
        return self.level >= 20

    def promote(self, promoted_class, promotion_info):
        if self.promoted:
            raise PromotionError("Unit already promoted")

        # Apply stat bonuses
        for stat, bonus in promotion_info["stat_bonus"].items():
            setattr(self, stat, getattr(self, stat) + bonus)
            if stat == "hp":
                self.max_hp += bonus
                self.hp += bonus

        # Swap class
        self.unit_class = promoted_class
        self.promoted = True

        if promotion_info.get("level_reset"):
            self.level = 1
            self.exp = 0

        print(f"✨ {self.name} promoted to {self.__class__.__name__}!")

    def promote_from_table(self, ignore_level=False):
        base = self.base_class_name

        if base not in PromotionData.REGISTRY:
            raise ValueError("This class cannot promote")

        promoted_name = list(PromotionData.REGISTRY[base].keys())[0]
        promotion_info = PromotionData.REGISTRY[base][promoted_name]

        # 🔥 Lazy import to avoid circular dependency
        from entities import classes

        promoted_class = getattr(classes, promoted_name)

        self.promote(promoted_class, promotion_info)
        
    def equip_class_skill(self, skill):
        if not hasattr(self, "ALLOWED_SKILLS"):
            raise ValueError(f"{self.__class__.__name__} cannot equip class skills")

        if skill not in self.ALLOWED_SKILLS:
            raise ValueError(
                f"{skill.name} is not allowed for {self.__class__.__name__}"
            )

        self.equip_skill(skill)



    