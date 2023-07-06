class User:
    name = "UserName"
    age = 15

    def say_name(self):
        return print(f"Hi my name is {self.name} and I am {self.age} years old.")

    def set_age(self, age):
        self.age = age


class Gamer(User):
    nik = "SomeNik"
    game = "Mario"

    def add_nik(self, nik):
        self.nik = nik

    def show_level(self):
        return f"My level is {self.level}"


roll = Gamer()
roll.name = "Vlad"
roll.add_nik("Rollo")
roll.set_age(37)
print(roll.say_name())


class SuperGamer(Gamer):
    level = "noob"


azira = SuperGamer()
azira.level = "Piypiy"
print(roll.show_level())
