from ex_01 import User

class Hotel:
    def __init__(self, room_counter):
        self.rooms_counter = room_counter
        self.book_room = {}
    
    def __call__(self, value:User):
        if len(self.book_room) < self.rooms_counter:
            self.book_room[value.name] = value
            return f"{value.name} book room success"
        return "No free room"


hotel = Hotel(2)

user = User("Marry")
user_1 = User("Gerry")
user_2 = User("Bill")

print(hotel(user))
print(hotel(user_1))
print(hotel(user_2))


print(hotel.book_room)

