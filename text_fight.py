# TODO
# Add potion action - heal ✅
# Add critical hit chance and damage ✅
# Add dodge chance ✅
# Add level up - Exp - Upgrade stats✅
# Add shop
# Add names and create boss
# Add spells
# Add thorn defend action
# Save and load player stats ---
# Add turns taken and enemies defeated
# Inheritance
import random
from Player import Player
from Enemy import Enemy

enemies = [
    Enemy(2,2,0,2),
    Enemy(5,3,1,10),
    Enemy(10,4,2,20)
]
# ======================== Main Game ========================
player_name = input("Enter your name: ")
player = Player(player_name)
# Game Rounds
game_round = 1
for enemy in enemies:
    print(f"========== New Enemy Appears! ==========")
    enemy.show_stats()
    while player.is_alive() and enemy.is_alive():
        # Player turn

        print(f"Round:{game_round}")
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
                game_round +=1
                break

            # Enemy turn
            enemy.attack(player)
            game_round += 1
            if not player.is_alive():
                print("Game over")
                break
        # ====== Heal Option ======
        elif choice == 'h':
            game_round += 1
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