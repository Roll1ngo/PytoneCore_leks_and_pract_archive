from collections import UserDict


class MyDict(UserDict):
    def __add__(self, other):
        self.data.update(other)
        return self


def __sub__(self, other):
    print(self, other)
    for key in other:
        if key in other:
            self.data.pop(key)
    return self


d1 = MyDict({1: "a", 2: "b"})
d2 = MyDict({3: "c", 4: "d"})

d3 = d1 + d2
d4 = d3 - d2
print(d4)
