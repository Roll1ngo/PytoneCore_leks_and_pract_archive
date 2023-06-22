from collections import namedtuple

Cat = namedtuple("Cat",["nickname", "age", "owner"])

barsik = Cat("Barsik", 4, "Perry")

print(barsik.age)