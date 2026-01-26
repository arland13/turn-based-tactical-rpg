from combat.faction_phase import Faction
from combat.battle import BattleSystem

def enemy_phase(grid):
    grid.reset_phase_units(Faction.ENEMY)

    for unit in grid.unit_positions:
        if unit.faction != Faction.ENEMY:
            continue

        enemies = grid.get_enemies_in_range(unit, unit.weapon)
        if enemies:
            BattleSystem.battle(unit, enemies[0])

        unit.has_acted = True
