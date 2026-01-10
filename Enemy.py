import random
#  ============================== Enemy Class ==============================
# ===========================================================================
class Enemy:
    #   Constructor
    def __init__(self,health,damage,armor,experience):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.experience = experience
        # self.coins = coins
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
