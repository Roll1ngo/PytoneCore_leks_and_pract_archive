class Peoples:
    def __init__(self, peoples:list):
        self.values = peoples
    
    def __setitem__(self, idx, value):
        self.values.insert(idx, value)


list_of_peoples = ["Bill", "Sara", "Jill"]

peoples = Peoples(list_of_peoples)

peoples[2] = "Gerry"

print(peoples.values)

for p in peoples.values:
    print(p)

print(globals())