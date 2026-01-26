from combat.battle import BattleSystem

def player_action_menu(unit, grid):
    while True:
        print("\nChoose action:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Wait")

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

            BattleSystem.battle(unit, target)
            return

        elif choice == "2":
            if not unit.inventory:
                print("No items.")
                continue

            for i, item in enumerate(unit.inventory):
                print(f"{i+1}. {item.name}")

            try:
                idx = int(input("Choose item: ")) - 1
                unit.use_item(unit.inventory[idx])
                return
            except Exception as e:
                print(e)

        elif choice == "3":
            print(f"{unit.name} waits.")
            return
