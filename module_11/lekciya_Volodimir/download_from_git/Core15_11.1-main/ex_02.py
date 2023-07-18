from ex_01 import User, Phone

class Gamer:
    def __init__(self, user, games) -> None:
        self.user = user
        self.games:list = games
    
    def __getitem__(self, index):
        try:
            return self.games[index]
        except IndexError:
            return f"No game with index {index}"
    
    def __setitem__(self, index, value):
        self.games.insert(index, value)


user = User("Leonid", phone=Phone("+67384981928"))
gamer = Gamer(user, ["Age of Empires", "Heroes III"])

print(gamer[10])

gamer[-1] = "Cossacks"

print(gamer.games)

print(gamer.user)