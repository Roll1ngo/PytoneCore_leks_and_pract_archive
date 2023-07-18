import collections
from random import randint

class My_list(collections.UserList):

    def append(self):
        print("No element for you")

    def say_hello(self):
        print(f"Hello from {self.data}")
    
    def update_with_random(self):
        self.data[randint(0,len(self.data)-1)] = randint(0,10)
        return self.data


some_list = My_list("Hello")
print(some_list.update_with_random())


