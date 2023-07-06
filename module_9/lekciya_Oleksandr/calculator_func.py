# x = int(input("x: "))
# y = int(input("y: "))
# operator = input("operator")

# def operate(x,y,operator):
#     if operator == "+":
#         return x+y
#     elif operator == "-":
#         return x-y
#     elif operator == "*":
#         return x*y
#     elif operator == "/":
#         return x/y
    
# print(operate(10,5,"+"))

from math import cos
def summ(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

operations = {"+":summ, "-":sub, "*": mul, "cos": cos}
print(operations["+"](5,10))

def operate(operator):
    return operations[operator]

handler_sum= operate("+")
print(operate("cos")(30))







