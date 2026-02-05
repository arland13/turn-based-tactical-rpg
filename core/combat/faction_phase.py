from enum import Enum, auto

class Phase(Enum):
    PLAYER = auto()
    ENEMY = auto()
    ALLY = auto()

class Faction(Enum):
    PLAYER = auto()
    ENEMY = auto()
    ALLY = auto()

class PhaseManager:
    def __init__(self):
        self.current_phase = Phase.PLAYER

    def __str__(self):
        return f"\n=== {self.current_phase.name} PHASE ==="

    def next_phase(self):
        if self.current_phase == Phase.PLAYER:
            self.current_phase = Phase.ENEMY
        elif self.current_phase == Phase.ENEMY:
            self.current_phase = Phase.ALLY
        else:
            self.current_phase = Phase.PLAYER

def is_hostile(a, b):
    if a == Faction.ENEMY and b in (Faction.PLAYER, Faction.ALLY):
        return True
    if b == Faction.ENEMY and a in (Faction.PLAYER, Faction.ALLY):
        return True


if __name__ == "__main__":
    phase_manager = PhaseManager()
    print(phase_manager)
    
    

