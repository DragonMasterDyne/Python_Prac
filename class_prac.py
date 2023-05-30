class Player:
    def __init__(self, base_health, base_magic, base_armor, base_stamina, base_movement):
        self.base_health = base_health
        self.base_magic = base_magic
        self.base_armor = base_armor
        self.base_stamina = base_stamina
        self.base_movement = base_movement

    def basic_strike(self):
        self.damage = 5
        print("You did 5 damage!")

class Mage_player_class(Player):
    def __init__(self, base_health = 80, base_magic = 50, base_armor = 6, base_stamina = 65, base_movement = 4):
        super().__init__(base_health, base_magic, base_armor, base_stamina, base_movement)
        self.player_health = base_health
        self.player_magic = base_magic
        self.remainder = self.player_magic

    def staff_bash(self):
        self.damage = 5

    def focus_blast(self):
        self.damage = 12
        self.remainder = self.player_magic - 5
        print("You have " + str(self.remainder) + " left.")

    def meditate(self):
        print(str(self.player_magic))
        restore_mana = self.remainder + 10
        print("Your mana is at " + str(restore_mana))

class Worrior(Player):
    def __init__(self, base_health = 120, base_magic = 30, base_armor = 12, base_stamina = 80, base_movement = 5):
        super().__init__(base_health, base_magic, base_armor, base_stamina, base_movement)
        self.player_heath = base_health
        self.player_magic = base_magic
        self.player_stamina = base_stamina

    def heavystrike(self):
        self.damage = 8 

    def triple_strike(self):
        self.damage = 15
        self.player_stamina = self.player_stamina - 50


m = Mage_player_class()
print(vars(m))
f = Mage_player_class().focus_blast

f()

