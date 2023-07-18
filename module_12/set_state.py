import pickle

class Human:
    def __init__(self, name):
        self.name = name

    def __getstate__(self) -> object:
        data = self.__dict__
        data["age"] = 10
        return self
    
human = Human("Dre")
data_str = pickle.dumps(human)

print(data_str)

