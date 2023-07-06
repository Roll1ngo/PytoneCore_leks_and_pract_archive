class A:
    x = "I am exist in class A"


class B:
    b = " I am only class B"
    x = "I am exist in class B"


class C(B, A):
    z = "This exist only class C"


obj_c = C()

print(obj_c.b)
