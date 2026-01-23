from entities.classes import Myrmidon
from skills.skill_lists import Skill_registry
from maps.grid import Grid
from weapons.weapon_lists import WeaponRegistry
from combat.battle import BattleSystem

# ======================
# DEMO / TEST
# ======================

if __name__ == "__main__":
    hero = Myrmidon("Aldo", "A")
    print(hero.show_stat())
    enemy = Myrmidon("Rika", "R")
    weapon = WeaponRegistry()
    skill = Skill_registry
    hero.equip_weapon(weapon.iron_sword)
    hero.equip_class_skill(skill.ASTRA)
    
   
    grid = Grid(10, 10)
    grid.place_unit(4, 4, hero)
    grid.place_unit(1, 6, enemy)
    

    print("\nMovement range for Aldo:")
    movable = grid.get_movable_tiles(hero)
    grid.render(highlight=movable)
    command1, command2 = map(int, input("Enter column and row (e.g. 3 5): ").split())

    print(f"\nMove Aldo to ({command2}, {command1})\n")
    grid.move_unit(hero, command2, command1)
    grid.render()
    
    # --- AUTO COMBAT CHECK ---
    enemies = grid.get_enemies_in_range(hero, hero.weapon)

    if enemies:
        print("\nEnemies in range:")
        for i, enemy in enumerate(enemies):
            print(f"{i}. {enemy.name}")

        # Auto-pick first enemy (later: player choice)
        target = enemies[0]

        print(f"\n{hero.name} engages {target.name}!")
        BattleSystem.battle(hero, target)
    else:
        print("\nNo enemies in range.")