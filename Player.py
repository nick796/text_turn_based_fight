#  ============================== Player Class ==============================
# ===========================================================================
import random
import time
from Spellbook import *
class Player:
    #   Constructor
    def __init__(self,name):
        # Base stats
        self.name = name
        self.health = 10
        self.damage = 3 # for random
        self.armor = 0
        # For heal
        self.number_potions = 5
        # For special effects
        self.critical_chance = 0.2
        self.dodge = 0.2
        # for level
        self.level = 1
        self.current_experience = 0
        self.max_experience = 1

        self.player_spellbook = Spellbook()
        self.coins = 0

    #    Methods
    def attack(self,enemy):
        print("======== Player Action ===========")
        hit_damage_value = random.randint(1,self.damage)
        # Critical Hit
        if random.random()< self.critical_chance:
            hit_damage_value *=2
            print(f"{self.name} did a critical hit")

        print(f"{self.name} attack Enemy for {hit_damage_value} damage!")

        enemy.got_hit(hit_damage_value)

    def defend(self,enemy,damage_enemy):
        damage_reflect = damage_enemy//2
        print(f"You reflect {damage_reflect} damage to the enemy! ")
        enemy.got_hit(damage_reflect)
        self.got_hit(damage_reflect)


    def got_hit(self,damage):
        # Dodge chance
        if random.random()<self.dodge:
            print(f"{self.name} dodged the attack")

            return
        real_damage = damage - self.armor
        if real_damage < 0:
            real_damage = 0
        self.health -= real_damage
        print(f"{self.name} got hit for {real_damage} damage!\n")


    # Heal-Potion function
    def use_potion(self):
        self.health += 5
        if self.health>10:
            self.health = 10
        print("======== Player Action ===========")
        print(f"You healed for 5")

    def level_up(self):
        self.level +=1
        self.max_experience *=2
        self.current_experience = 0

        self.health = self.level*10
        self.damage = self.damage + 1
        self.armor +=1

        self.number_potions +=1
    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def show_stats(self):
        print(f"name:{self.name}\nhealth:{self.health}\ndamage:{self.damage}\narmor:{self.armor}")
