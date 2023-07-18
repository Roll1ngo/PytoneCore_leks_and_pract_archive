class Hotel:
    def __init__(self, rooms) -> None:
        self.rooms = rooms
    
    def __add__(self, __obj):
        return Hotel(self.rooms + __obj.rooms)
        

hotel1 = Hotel(20)
hotel2 = Hotel(10)

print(type((hotel1 + hotel2)))