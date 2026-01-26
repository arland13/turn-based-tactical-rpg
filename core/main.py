from entities.classes import Myrmidon
from skills.skill_lists import Skill_registry
from maps.grid import Grid
from weapons.weapon_lists import WeaponRegistry
from combat.faction_phase import Phase, Faction, PhaseManager
import player_phase as pp, enemy_phase as ep

# ======================
# DEMO / TEST
# ======================

def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("please input number!")

if __name__ == "__main__":
    hero1 = Myrmidon("Aldo", "A", Faction.PLAYER)
    print(hero1.show_stat())

    hero2 = Myrmidon("Rika", "R", Faction.PLAYER)
    enemy2 = Myrmidon("Indah", "I", Faction.ENEMY)
    enemy3 = Myrmidon("Silvia", "S", Faction.ENEMY)

    weapon = WeaponRegistry()
    skill = Skill_registry

    hero1.equip_weapon(weapon.iron_sword)
    hero1.equip_class_skill(skill.ASTRA)

    hero2.equip_weapon(weapon.iron_sword)
    hero2.equip_class_skill(skill.ASTRA)

    enemy2.equip_weapon(weapon.iron_sword)
    enemy2.equip_class_skill(skill.ASTRA)

    enemy3.equip_weapon(weapon.iron_sword)
    enemy3.equip_class_skill(skill.ASTRA)
    grid = Grid(10, 10)
    grid.place_unit(4, 4, hero1)
    grid.place_unit(1, 6, hero2)
    grid.place_unit(2, 7, enemy2)
    grid.place_unit(3, 6, enemy3)
    phase_manager = PhaseManager()
    
    while True:
        print(phase_manager)

        if phase_manager.current_phase == Phase.PLAYER:
            pp.player_phase(grid)
            phase_manager.next_phase()

        elif phase_manager.current_phase == Phase.ENEMY:
            ep.enemy_phase(grid)
            phase_manager.next_phase()

        else:
            phase_manager.next_phase()
