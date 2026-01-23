from weapons.weapon import Weapon
from weapons.weapon_types import WeaponType

class WeaponRegistry:
    iron_sword = Weapon(
    name="Iron Sword",
    weapon_type=WeaponType.SWORD,
    might=5,
    hit=90,
    weight=5,
    min_range=1,
    max_range=1
    )

    iron_axe = Weapon(
    name="Iron Axe",
    weapon_type=WeaponType.AXE,
    might=8,
    hit=70,
    weight=10,
    min_range=1,
    max_range=1
    )