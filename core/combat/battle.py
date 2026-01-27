import random
from skills.skill_lists import Skill_registry

class BattleSystem:
    @staticmethod
    def attack(attacker, defender):
        weapon = attacker.weapon
        if not weapon:
            print(f"{attacker.name} has no weapon!")
            return
        
        print(f"{attacker.name} attacks {defender.name}!")

        # HIT CHECK
        hit = weapon.hit + attacker.skl * 2 + attacker.lck
        avoid = defender.spd * 2 + defender.lck
        hit_rate = max(0, min(100, hit - avoid))

        if random.randint(1, 100) > hit_rate:
            print("Miss!")
            return

        # DAMAGE
        dmg = max(attacker.str + weapon.might - defender.def_, 0)

        # CRIT CHECK
        crit = attacker.skl // 2
        crit_avoid = defender.lck
        crit_rate = max(0, crit - crit_avoid)

        if random.randint(1, 100) <= crit_rate:
            dmg *= 3
            print("Critical Hit!")

        defender.hp = max(0, (defender.hp - dmg))
        print(f"{defender.name} takes {dmg} damage (HP: {defender.hp})")

    @staticmethod
    def battle(attacker, defender):
        # VANTAGE CHECK
        if (
            Skill_registry.VANTAGE in defender.skills and
            defender.hp <= defender.max_hp // 2
        ):
            print("Vantage activated!")
            BattleSystem.attack(defender, attacker)
            if attacker.hp == 0:
                print(f"{attacker.name} defeated!")
                return attacker

        # Normal attack
        BattleSystem.attack(attacker, defender)

        if defender.hp == 0:
            print(f"{defender.name} defeated!")
            attacker.gain_exp(40)  # 🔥 kill EXP
            return defender

        # Counterattack
        BattleSystem.attack(defender, attacker)
        if attacker.hp == 0:
            print(f"{attacker.name} defeated!")
            defender.gain_exp(40)
            return attacker

        # Follow-up
        if attacker.spd - defender.spd >= 4:
            print("Follow-up attack!")
            BattleSystem.attack(attacker, defender)
            if defender.hp == 0:
                print(f"{defender.name} defeated!")
                attacker.gain_exp(40)
                return defender

        # ❗ Battle happened but no kill
        attacker.gain_exp(10)
        return None