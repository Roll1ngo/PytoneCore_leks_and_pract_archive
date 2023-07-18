class A:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


a = A("1")
b = A(2)


print(b)
