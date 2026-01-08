# TODO
# Add potion action - heal
# Add critical hit chance and damage
# Add dodge chance
# Add names and create boss
# Add spells
# Add thorn defend action
# Add level up - Exp - Upgrade stats
# Save and load player stats ---
# Add turns taken and enemies defeated
# Inheritance
import random
class Player:
    #   Constructor
    def __init__(self,name):
        self.name = name
        self.health = 10
        self.damage = 3 # for random
        self.armor = 0
    #    Methods
    def attack(self,enemy):
        hit_damage_value = random.randint(1,self.damage)
        print("======== Player Action ===========")
        print(f"{self.name} attack Enemy for {hit_damage_value} damage!")
        enemy.got_hit(hit_damage_value)
    def got_hit(self,damage):
        real_damage = damage - self.armor
        if real_damage < 0:
            real_damage = 0
        self.health -= real_damage
        print(f"{self.name} got hit for {real_damage} damage!\n")
    def is_alive(self):
        if self.health < 0:
            return False
        else:
            return True

    def show_stats(self):
        print(f"name:{self.name}\nhealth:{self.health}\ndamage:{self.damage}\narmor:{self.armor}")


class Enemy:
    #   Constructor
    def __init__(self,health,damage,armor):
        self.health = health
        self.damage = damage
        self.armor = armor
    #   Methods
    def attack(self, player):
        hit = random.randint(1, self.damage)
        print("======== Enemy Action ===========")
        print(f"Enemy attacks {player.name} for {hit}!")
        player.got_hit(hit)

    def got_hit(self,damage):
        real_damage = damage - self.armor
        if real_damage < 0:
            real_damage = 0
        self.health -= real_damage
        print(f"Enemy got hit for {real_damage} damage!\n")
    def is_alive(self):
        return self.health > 0

    def show_stats(self):
        print(f"name:Enemy\nhealth:{self.health}\ndamage:{self.damage}\narmor:{self.armor}")

enemies = [
    Enemy(2,2,0),
    Enemy(5,3,1),
    Enemy(10,4,2)
]
# ======================== Main Game ========================
player_name = input("Enter your name: ")
player = Player(player_name)

for enemy in enemies:
    print(f"========== New Enemy Appears! ==========")
    enemy.show_stats()
    while player.is_alive() and enemy.is_alive():
        # Player turn
        choice = input("Attack or scan enemy? (a/s)").lower().strip()
        if choice == 's':
            print("=== Your Stats ===")
            player.show_stats()
            print("=== Enemy Stats ===")
            enemy.show_stats()
            continue

        player.attack(enemy)
        if not enemy.is_alive():
            print("Enemy defeated!")
            break

        # Enemy turn
        enemy.attack(player)
        if not player.is_alive():
            print("Game over")
            break

    if not player.is_alive():
        break
if player.is_alive():
    print("You defeated all the enemies")
else:
    print("Try next time ")