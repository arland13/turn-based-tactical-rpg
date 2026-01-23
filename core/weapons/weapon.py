class Weapon:
    def __init__(self, name, weapon_type, might, hit, weight, min_range, max_range):
        self.name = name
        self.weapon_type = weapon_type
        self.might = might
        self.hit = hit
        self.weight = weight
        self.min_range = min_range
        self.max_range = max_range

    def __repr__(self):
        return f"{self.name} ({self.weapon_type.value})"
