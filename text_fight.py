# TODO
# Add potion action - heal ✅
# Add critical hit chance and damage ✅
# Add dodge chance ✅
# Add level up - Exp - Upgrade stats✅
# Add shop ✅
# Add names and create boss
# Add spells ✅
# Add thorn defend action ✅
# Save and load player stats ---
# Add turns taken and enemies defeated
# Inheritance
import random
import time

from Player import Player
from Enemy import Enemy
from Shop import Shop
from Boss import Boss
enemies = [
    Enemy(2,2,0,2,10),
    Enemy(5,3,1,10,20),
    Boss(5,3,1,10,20),
    Enemy(10,4,2,20,30)
]
# ======================== Main Game ========================
print("============================================================")
print("================= Welcome To Text Fighters =================")
print("============================================================")
print("Whats your name Challenger?")
player_name = input("Enter your name: ")
player = Player(player_name)

game_shop = Shop()
# Game Rounds
game_floor = 1
for enemy in enemies:

    # Every 2 rounds you get A shop Level
    if game_floor%2==0:
        while True:
            print(f"==== Shop Level ===")
            game_shop.show_items()
            print(f"You have ({player.coins} coins) ")
            shop_choice = int(input("Give a Choice you want to buy: "))
            match shop_choice:
                case 1:
                    if player.coins >= game_shop.wood_sword_cost:
                        game_shop.wood_sword_number -= 1
                        player.damage +=2
                        print("You bought one wood sword. Your damage +2!")
                    else:
                        print("You dont have enough money")
                case 2:
                    if player.coins >= game_shop.stone_sword_cost:
                        game_shop.stone_sword_number -= 1
                        player.damage +=4
                        print("You bought one stone sword. Your damage +4!")
                    else:
                        print("You dont have enough money")
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
    if isinstance(enemy,Boss):
        print("This is a boss enemy")
    print("========= Enemy Stats =========")
    enemy.show_stats()
    while player.is_alive() and enemy.is_alive():
        # Player turn
        print(f"Floor:{game_floor}")
        choice = input(f"Write a for attack, s for scan enemy, h for heal and d for defend\nWrite sp for spellbook use\nWhats your action {player_name}?: ").lower().strip()

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
                print(f"You loot from the enemy {enemy.coins} coins!")
                player.coins += enemy.coins
                # Level Up Chance
                player.current_experience += enemy.experience
                if player.current_experience >= player.max_experience:
                    print("You leveled Up! Stats got stronger")
                    player.level_up()
            else:
                # Enemy turn
                enemy.attack(player)

            if not player.is_alive():
                print("Game over")

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
        #  ======== Defend ========
        elif choice == 'd':
            player.defend(enemy,enemy.damage)
        #  ======== Spellbook ========
        elif choice == 'sp':
            player.player_spellbook.show_spell_stats(enemy,player)


    if not enemy.is_alive():
        print(f"You kill the enemy!")
        game_floor += 1
    if not player.is_alive():
        break
if player.is_alive():
    print("You defeated all the enemies")
else:
    print("Try next time ")