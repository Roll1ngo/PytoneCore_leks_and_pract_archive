

class Character:
    count = 0
    hp = 100
    mp = 100
    
    def __init__(self, name,nik):
        self.left_hand = Weapon()
        self.right_hand = None
        Character.count+= 1
        self.name = name
        self.nik = nik

    def pick_weapon(self,weapon):
        if self.left_hand is None:
            self.left_hand = weapon
        elif self.right_hand is None:
            self.right_hand = weapon
        else:
            ("I am full")\
            
    def show_weapon(self):
        return self.right_hand, self.left_hand
        


    def move(self):
        print("I am moving")

    def identify(self):
        print(self.name)

    def show_nik(self):
        print(f"My nik is {self.nik}")

    def die(self):
        return self.left_hand, self.right_hand

class Weapon:
    def __init__(self):
        self .damage = 10

    def damage(self):
        return self.damage

char_1 = Character(name="Vadim", nik="Santa")
print(char_1.__dict__)

char_2 = Character("char_2", "Roll")

sword = Weapon()

char_1.pick_weapon(sword)

left_hand, right_hand =  char_1.die()

char_2.pick_weapon(left_hand)















    
