age = input("How old are you?:")
# greeting = f"Hello, {name}!"
# print(greeting)
age = int(age)
if age < 18:
    age = "adult"
    print(age)
if age > 18:
    age = "old"
    print(age)
