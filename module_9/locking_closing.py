def adder(val):
    def inner(x):
        return x+val
    return inner

two_adder = adder(2)
print(two_adder(3))

