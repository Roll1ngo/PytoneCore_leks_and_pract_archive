class A:
    def __init__(self):
        print("Hello, I am A")


class B(A):
    def __init__(self):
        super(). __init__()
        print("Hello, I am B")

b = B()
print(b)