# TODO
# Add potion action - heal ✅
# Add critical hit chance and damage ✅
# Add dodge chance ✅
# Add level up - Exp - Upgrade stats✅
# Add names and create boss
# Add spells
# Add thorn defend action
# Save and load player stats ---
# Add turns taken and enemies defeated
# Inheritance
import random
#  ============================== Player Class ==============================
# ===========================================================================
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
        if self.health < 0:
            return False
        else:
            return True

    def show_stats(self):
        print(f"name:{self.name}\nhealth:{self.health}\ndamage:{self.damage}\narmor:{self.armor}")

#  ============================== Enemy Class ==============================
# ===========================================================================
class Enemy:
    #   Constructor
    def __init__(self,health,damage,armor,experience):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.experience = experience
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
    Enemy(2,2,0,2),
    Enemy(5,3,1,10),
    Enemy(10,4,2,20)
]
# ======================== Main Game ========================
player_name = input("Enter your name: ")
player = Player(player_name)

for enemy in enemies:
    print(f"========== New Enemy Appears! ==========")
    enemy.show_stats()
    while player.is_alive() and enemy.is_alive():
        # Player turn
        choice = input("Attack,scan enemy,or heal? (a/s,h)").lower().strip()

        # ====== Scan Option ======
        if choice == 's':
            print("=== Your Stats ===")
            player.show_stats()
            print("=== Enemy Stats ===")
            enemy.show_stats()
            continue
        # ====== Attack Option ======
        elif choice == 'a':
            player.attack(enemy)
            if not enemy.is_alive():
                print("Enemy defeated!")
                print("You gain 1 experience")
                # Level Up Chance
                player.current_experience += enemy.experience
                if player.current_experience >= player.max_experience:
                    print("You leveled Up! Stats got stronger")
                    player.level_up()
                break

            # Enemy turn
            enemy.attack(player)
            if not player.is_alive():
                print("Game over")
                break
        # ====== Heal Option ======
        elif choice == 'h':
            if player.number_potions>0:
                player.use_potion()

                # Enemy turn
                enemy.attack(player)
                if not player.is_alive():
                    print("Game over")
                    break

            else:
                print(f"You dont have any potions left")
                continue
    if not player.is_alive():
        break
if player.is_alive():
    print("You defeated all the enemies")
else:
    print("Try next time ")