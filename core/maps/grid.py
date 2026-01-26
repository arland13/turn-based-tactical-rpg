from combat.battle import BattleSystem
from combat.faction_phase import Faction

class Tile:
    def __init__(self):
        self.unit = None

    def is_empty(self):
        return self.unit is None

    def place_unit(self, unit):
        if not self.is_empty():
            raise ValueError("Tile already occupied")
        self.unit = unit

    def remove_unit(self):
        unit = self.unit
        self.unit = None
        return unit


# ======================
# GRID SYSTEM
# ======================    

class Grid:
    def __init__(self, rows, cols):
        self.tiles = [[Tile() for _ in range(cols)] for _ in range(rows)]
        self.unit_positions = {}  # unit -> (row, col)

    # ---------- Placement ----------
    def place_unit(self, row, col, unit):
        self._validate_position(row, col)

        tile = self.tiles[row][col]
        tile.place_unit(unit)
        self.unit_positions[unit] = (row, col)

    # ---------- Movement Range ----------
    def get_movable_tiles(self, unit):
        if unit not in self.unit_positions:
            raise ValueError("Unit not on grid")

        start_row, start_col = self.unit_positions[unit]
        max_range = unit.mov

        reachable = []

        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                distance = abs(start_row - r) + abs(start_col - c)

                if distance <= max_range:
                    tile = self.tiles[r][c]
                    if tile.is_empty() or tile.unit is unit:
                        reachable.append((r, c))

        return reachable

    # ---------- Move Unit ----------
    def move_unit(self, unit, new_row, new_col):
        movable = self.get_movable_tiles(unit)

        if (new_row, new_col) not in movable:
            raise ValueError("Target out of movement range")


        old_row, old_col = self.unit_positions[unit]

        self.tiles[old_row][old_col].remove_unit()
        self.tiles[new_row][new_col].place_unit(unit)

        self.unit_positions[unit] = (new_row, new_col)

    # ---------- Rendering ----------
    def render(self, highlight=None):
        highlight = highlight or []

        print("\n   " + " ".join(f"{i:2}" for i in range(len(self.tiles[0]))))
        print("   " + "---" * len(self.tiles[0]))

        for r, row in enumerate(self.tiles):
            line = f"{r:2}|"
            for c, tile in enumerate(row):
                if (r, c) in highlight and tile.is_empty():
                    line += " * "
                elif tile.unit:
                    line += f" {tile.unit.symbol} "
                else:
                    line += " . "
            print(line)

    # ---------- Utilities ----------
    def _validate_position(self, row, col):
        if row < 0 or col < 0:
            raise ValueError("Negative position")
        if row >= len(self.tiles) or col >= len(self.tiles[0]):
            raise ValueError("Position out of bounds")
        
    def get_enemies_in_range(self, attacker, weapon):
        if attacker not in self.unit_positions:
            raise ValueError("Unit not on grid")

        ar, ac = self.unit_positions[attacker]
        targets = []

        for unit, (ur, uc) in self.unit_positions.items():
            if unit is attacker:
                continue

            # 🔑 FACTION CHECK
            if unit.faction == attacker.faction:
                continue

            distance = abs(ar - ur) + abs(ac - uc)
            if weapon.min_range <= distance <= weapon.max_range:
                targets.append(unit)

        return targets
    
    def reset_phase_units(self, faction):
        for unit in self.unit_positions:
            if unit.faction == faction:
                unit.has_acted = False

    def enemy_phase(self):
        for unit in self.unit_positions:
            if unit.faction != Faction.ENEMY:
                continue

            enemies = self.get_enemies_in_range(unit, unit.weapon)
            if enemies:
                BattleSystem.battle(unit, enemies[0])


    


    