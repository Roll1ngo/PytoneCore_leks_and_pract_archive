import copy

class Animal:
    def __init__(self,type,age):
        self.type = type
        self.age = age

    def __copy_(self):
        print("in copy")

    def __deepcopy__(self,memo):
        print("in deep copy")

animal = Animal("Duck",2)

copy.copy(animal)

copy.deepcopy(animal)