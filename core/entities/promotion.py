class PromotionError(Exception):
    pass

class PromotionData:
    """
    Defines promotion paths & bonuses
    """
    REGISTRY = {
        "Myrmidon": {
            "Swordmaster": {
                "stat_bonus": {
                    "hp": 3,
                    "str": 2,
                    "skl": 2,
                    "spd": 2,
                    "def_": 1,
                    "res": 1,
                },
                "level_reset": True
            } }
    }


