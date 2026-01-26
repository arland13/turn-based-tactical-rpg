from combat.faction_phase import Faction
from helper_function import player_action_menu

def player_phase(grid):
    grid.reset_phase_units(Faction.PLAYER)

    while True:
        available_units = [
            u for u in grid.unit_positions
            if u.faction == Faction.PLAYER and not u.has_acted
        ]

        if not available_units:
            break  # End Player Phase

        unit = available_units[0]  # cursor later
        movable_tiles = grid.get_movable_tiles(unit)

        grid.render(highlight=movable_tiles)

        try:
            r, c = map(int, input(f"{unit.name} move to (row col): ").split())
            grid.move_unit(unit, r, c)
        except ValueError as e:
            print(e)
            continue

        player_action_menu(unit, grid)
        unit.has_acted = True
