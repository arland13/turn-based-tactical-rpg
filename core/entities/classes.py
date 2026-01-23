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
    
    def __init__(self, name, symbol):
        super().__init__(name,symbol,
                         hp=16, max_hp=16,
                         str=5, mag=0,
                         skl=9, spd=10,
                         lck=6, def_=4,
                         res=1, mov=6,)
        self.level = 1
        self.exp = 0
        self.exp_to_next = 100
        
    def equip_class_skill(self, skill):
        if skill in self.ALLOWED_SKILLS:
            self.equip_skill(skill)
        else:
            raise ValueError("Skill not allowed for Myrmidon")