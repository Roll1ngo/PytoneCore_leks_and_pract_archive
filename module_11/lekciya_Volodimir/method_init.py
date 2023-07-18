class User:

    def __init__(self,name):
        self.name =name

    def __str__(self)->str:
        return self.name
        



user_vlad = User("Vlad")
user_santa = User("Santa")
print(user_vlad, user_santa)

