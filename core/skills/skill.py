from enum import Enum

class SkillType(Enum):
    PASSIVE = "passive"
    ACTIVE = "active"
    
class Skill:
    def __init__(self, name, description, skill_type):
        self.name = name
        self.description = description
        self.skill_type = skill_type

    def __str__(self):
        return f"{self.name} ({self.skill_type.value})"
    


    