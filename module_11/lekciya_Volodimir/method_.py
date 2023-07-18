

class Gamer:
    def __init__(self,user, games)->None:
        self.user = user
        self.games = list(games)

user = User("Leonid", phone = Phone("+3898989898"))

gamer = Gamer(user,["Age of Empires","Heroes III"])

print(gamer.games[0])

