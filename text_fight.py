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
from Shop import Shop
enemies = [
    Enemy(2,2,0,2),
    Enemy(5,3,1,10),
    Enemy(10,4,2,20)
]
# ======================== Main Game ========================
player_name = input("Enter your name: ")
player = Player(player_name)

game_shop = Shop()
# Game Rounds
game_round = 1
for enemy in enemies:
    # Every 2 rounds you get A shop Level
    if game_round%2==0:
        while True:
            print(f"==== Shop Level ===")
            game_shop.show_items()
            shop_choice = int(input("Give a Choice you want to buy: "))
            match shop_choice:
                case 1:
                    game_shop.wood_sword_number -= 1
                    player.damage +=2
                    print("You bought one wood sword. Your damage +2!")
                case 2:
                    game_shop.stone_sword_number -= 1
                    player.damage +=4
                    print("You bought one stone sword. Your damage +4!")
                case 3:
                    game_shop.wood_armor_set_number -=1
                    player.armor += 1
                    print("You bought one wood armor set. Your armor +1!")
                case 4:
                    game_shop.stone_armor_set_number -=1
                    player.armor += 2
                    print("You bought one stone armor set. Your armor +2!")
                case 5:
                    game_shop.heal_potions_number -= 1
                    player.number_potions += 5
                    print("You bought x5 heal potions.")
            break
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