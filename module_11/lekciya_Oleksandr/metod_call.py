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

    def __getitem__(self, index):
        return self.position[index]

    def __setitem__(self, key, value):
          self.position[key] = value

    def __call__(self):
        print("This object has been called")


char_position = Position(2,4)
print(char_position())



        