from combat.battle import BattleSystem
from combat.faction_phase import is_hostile

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_closest_enemy(unit, grid):
    ux, uy = grid.unit_positions[unit]

    enemies = [
        u for u in grid.unit_positions
        if is_hostile(unit.faction, u.faction)
    ]

    if not enemies:
        return None

    enemies.sort(
        key=lambda e: abs(ux - grid.unit_positions[e][0] +
                      abs(uy - grid.unit_positions[e][1]))
    )
    return enemies[0]

def move_towards(unit, target, grid):
    ux, uy = grid.unit_positions[unit]
    tx, ty = grid.unit_positions[target]

    movable_tiles = grid.get_movable_tiles(unit)

    # Choose tile that minimizes distance to target
    best_tile = min(
        movable_tiles,
        key=lambda t: abs(t[0] - tx) + abs(t[1] - ty)
    )

    grid.move_unit(unit, best_tile[0], best_tile[1])

def player_action_menu(unit, grid):
    while True:
        print("\nChoose action:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Wait")
        print("4. Show Stat")

        choice = input("> ")

        if choice == "1":
            enemies = grid.get_enemies_in_range(unit, unit.weapon)
            if not enemies:
                print("No enemies in range.")
                continue

            print("\nChoose target:")
            for i, enemy in enumerate(enemies):
                print(f"{i+1}. {enemy.name} (HP {enemy.hp})")

            try:
                idx = int(input("> ")) - 1
                target = enemies[idx]
            except (ValueError, IndexError):
                print("Invalid target.")
                continue

            result = BattleSystem.battle(unit, target)
            if result:
                grid.unit_lose(result)

            return  # action ends here

        elif choice == "2":
            if not unit.inventory:
                print("No items.")
            else:
                print(f"\n{unit.show_items()}")
                continue
        
        elif choice == "3":
            print(f"{unit.name} waits.")
            return
        
        elif choice == "4":
            print(f"\n{unit.show_stat()}")

        else:
            print("Invalid choice.")
