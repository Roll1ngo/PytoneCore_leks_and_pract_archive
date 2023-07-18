class MyDict:
    def __init__(self):
        self.data = {"a":1,"b":2}

    def __setitem__(self,key,value):
        if key in self.data:
            print(self.data[key])
            self.data[key].append(value)
        else:
            self.data[key] = [value]

my_dict = MyDict()
my_dict["c"] = 3
my_dict["c"] = 4



print(my_dict.data)