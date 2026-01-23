class Character:
    def __init__(
        self,
        name,
        symbol,
        hp,
        max_hp,
        str,
        mag,
        skl,
        spd,
        lck,
        def_,
        res,
        mov
    ):
        self.name = name
        self.symbol = symbol
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
        
    def show_stat(self):
        return (
            f"Name : {self.name}\t"f"Hp   : {self.hp}\n"
            f"Str  : {self.str}\t"f"Mag  : {self.mag}\n"
            f"Skl  : {self.skl}\t"f"Spd  : {self.spd}\n"
            f"Lck  : {self.lck}\t"f"Def  : {self.def_}\n"
            f"Res  : {self.res}\t"f"Mov  : {self.mov}"
            )
    
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
       