class Shop:
    def __init__(self):
        self.wood_sword_number = 1
        self.wood_sword_cost = 10
        self.stone_sword_number = 1
        self.stone_sword_cost = 20

        self.wood_armor_set_number =1
        self.wood_armor_set_cost = 10
        self.stone_armor_set_number = 1
        self.stone_armor_set_cost = 20

        self.heal_potions_number = 20
        self.heal_potions_cost = 1
    def show_items(self):
        print("=========== Weapons ===========")
        print(f"1) Wood Sword: {self.wood_sword_number}\nCost: {self.wood_sword_cost}\n\n2) Stone Sword: {self.stone_sword_number}\nCost: {self.stone_sword_cost}")
        print("=========== Armor ===========")
        print(f"3) Wood Armor: {self.wood_armor_set_number}\nCost: {self.wood_armor_set_cost}\n\n4) Stone Armor: {self.stone_armor_set_number}\nCost: {self.stone_armor_set_cost}")
        print("=========== Potions ===========")
        print(f"5) Health_Potions(x5): {self.heal_potions_number}\nCost: {self.heal_potions_cost}")


