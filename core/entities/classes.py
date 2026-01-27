from entities.character import Character
from skills.skill_lists import Skill_registry
from weapons.weapon_types import WeaponType

class Myrmidon(Character):
    ALLOWED_SKILLS = [
        Skill_registry.ASTRA,
        Skill_registry.VANTAGE
    ]
    ALLOWED_WEAPONS = [
        WeaponType.SWORD
    ]

    BASE_STATS = {
        "hp": 16,
        "str": 5,
        "mag": 0,
        "skl": 9,
        "spd": 10,
        "lck": 6,
        "def_": 4,
        "res": 1,
        "mov": 6,
    }

    GROWTHS = {
        "hp": 70,
        "str": 40,
        "mag": 10,
        "skl": 60,
        "spd": 65,
        "lck": 45,
        "def_": 30,
        "res": 20,
    }

    def __init__(self, name, symbol, faction, level=1):
        super().__init__(
            name=name,
            symbol=symbol,
            faction=faction,
            has_acted=False,
            hp=self.BASE_STATS["hp"],
            max_hp=self.BASE_STATS["hp"],
            str=self.BASE_STATS["str"],
            mag=self.BASE_STATS["mag"],
            skl=self.BASE_STATS["skl"],
            spd=self.BASE_STATS["spd"],
            lck=self.BASE_STATS["lck"],
            def_=self.BASE_STATS["def_"],
            res=self.BASE_STATS["res"],
            mov=self.BASE_STATS["mov"],
        )

        self.level = 1
        self.exp = 0
        self.exp_to_next = 100

        # Auto-level to requested level
        for _ in range(level - 1):
            self.level_up()

class Swordmaster(Character):
    ALLOWED_WEAPONS = [WeaponType.SWORD]

    BASE_STATS = {}  # not used (promotion only)
    GROWTHS = {
        "hp": 60,
        "str": 45,
        "mag": 5,
        "skl": 70,
        "spd": 70,
        "lck": 40,
        "def_": 25,
        "res": 25,
    }

    def __init__(self, name, symbol, faction, level=1):
        super().__init__(
            name=name,
            symbol=symbol,
            faction=faction,
            has_acted=False,
            hp=self.BASE_STATS["hp"],
            max_hp=self.BASE_STATS["hp"],
            str=self.BASE_STATS["str"],
            mag=self.BASE_STATS["mag"],
            skl=self.BASE_STATS["skl"],
            spd=self.BASE_STATS["spd"],
            lck=self.BASE_STATS["lck"],
            def_=self.BASE_STATS["def_"],
            res=self.BASE_STATS["res"],
            mov=self.BASE_STATS["mov"],
        )

        self.level = 1
        self.exp = 0
        self.exp_to_next = 100

        # Auto level-up to target level
        for _ in range(level - 1):
            self.level_up()
        
   