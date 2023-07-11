

class Character:
    count = 0
    hp = 100
    mp = 100
    
    def __init__(self, name,nik):
        self.left_hand = None
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
        self.dead = True

class Weapon:
    def __init__(self):
        self.type = "sword"
        self.damage  = 10

char_3 = Character(name="Vadim", nik="Santa")

#open chest

sword_1 = Weapon()
char_3.pick_weapon(sword_1)
left_hand, right_hand = char_3.show_weapon()







    
