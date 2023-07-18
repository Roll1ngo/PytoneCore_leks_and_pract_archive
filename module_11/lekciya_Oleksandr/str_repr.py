class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"__str__({self.x},{self.y})"

    
    def move_position(self,move_x:int,move_y:int)->int:
        return self.x+move_x, self.y + move_y
    
    def __repr__(self):
        return f"__repr__({self.x},{self.y})"
    
if __name__== "__main__":
    

    char_position = Position(1,3)

    print(str(char_position))
    print(char_position)
    a =char_position
    print(a)




