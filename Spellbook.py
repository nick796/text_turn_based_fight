import random
class Spellbook:
    def __init__(self):
        self.mana = 100
        self.spellLevel = 1
    def fireball(self,enemy):
        if self.mana <=0:
            print(f"You dont have enough mana")
            return
        magic_damage = random.randint(1,5)
        print(f"You cast fireball to the enemy")
        enemy.got_hit(magic_damage)
        self.mana = max(0,self.mana-20)
    def heal_fountain(self,player) :
        if self.mana <=0:
            print(f"You dont have enough mana!")
            return
        heal_portion = random.randint(5,10)
        print(f"You gain {heal_portion} health")
        player.health += heal_portion
        self.mana = max(0,self.mana -40)

    def show_spell_stats(self):
        print(f"fireball → 20 mana (1-5 damage)\nheal_fountain → 40 mana (5-10 heal)\nYou have {self.mana} mana left")