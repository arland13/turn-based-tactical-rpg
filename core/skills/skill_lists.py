from skills.skill import SkillType, Skill


class Skill_registry:
    # Myrmidon-themed skills        
    VANTAGE = Skill(
        "Vantage",
        "Strikes first when HP is below 50%",
        SkillType.PASSIVE
    )

    ASTRA = Skill(
        "Astra",
        "5 rapid attacks at reduced damage",
        SkillType.ACTIVE
    )


