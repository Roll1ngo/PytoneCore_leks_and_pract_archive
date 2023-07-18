class Human:
    name = "Public"
    _name = "Protected"
    __name = "Private"

human = Human()

print(human.name, human._name, human._Human__name)

human.name = "__Public"
human._name = "__Protected"
human._Human__name = "__Private"

print(human.name, human._name, human._Human__name)


