from ex_01 import User

class Human:
    def __init__(self, age):
        self.age = age
    
    def __eq__(self, other):
        if isinstance(other, Human):
            return self.age == other.age
        raise TypeError
    
    def __gt__(self, __other):
        return self.age > __other.age
    
    def __ge__(self, __other):
        return self.age >= __other.age 


hum1 = Human(22)
hum2 = Human(23)

user = User("Bill")

print(hum1 == user)