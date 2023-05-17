name = input("Enter yout name:")
age = input("Enter yout age:")
age = int(age)
has_driver_licence = True

if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")
else:
    print(f"User {name} can't rent a car")
