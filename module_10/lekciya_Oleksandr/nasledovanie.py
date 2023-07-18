class A:
    def hello(self):
        print("hello A")
class B(A):
    def hello(self):
        print("hello B")
class C:
    def hello(self):
        print("hello C")

class D(B,C):
    pass

print(D.hello())
