

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = [self.x, self.y]

    def __str__(self):
        return f"__str__({self.x},{self.y})"

    def move_position(self, move_x: int, move_y: int) -> int:
        return self.x+move_x, self.y + move_y

    def __repr__(self):
        return f"__repr__({self.x},{self.y})"
    
    def __getitem__(self,index):
        return self.position[index if  isinstance(index,int) else  "need int"]
    
    def __setitem__(self,key,value):
        if key <=len(self.position):
            self.position[key] = value
        else:
            raise IndexError("Ups")



char_position = Position(1, 3)
a= char_position.__new__(12,15)

print(a)
