class Human:
    def __init__(self,age):
        self.__age = None
        self.age  = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age (self,value):
        if 0<value<100:
            self.__age = value
        else:
            print("Bad value")

hum1 = Human(55)
hum2 = Human(0)
hum3 = Human(101)