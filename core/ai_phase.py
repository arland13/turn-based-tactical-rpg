from combat.battle import BattleSystem
from helper_function import find_closest_enemy, move_towards

def ai_phase(grid, faction):
    grid.reset_phase_units(faction)

    for unit in list(grid.unit_positions.keys()):
        if unit.faction != faction or unit.has_acted:
            continue

        target = find_closest_enemy(unit, grid)
        if not target:
            unit.has_acted = True
            continue

        # Move first
        move_towards(unit, target, grid)

        # Attack if possible
        enemies = grid.get_enemies_in_range(unit, unit.weapon)
        if enemies:
            result = BattleSystem.battle(unit, enemies[0])
            if result:
                grid.unit_lose(result)

        unit.has_acted = True
