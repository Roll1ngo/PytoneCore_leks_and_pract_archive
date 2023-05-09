is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")
is_active = bool(is_active)
is_admin = bool(is_admin)
is_permission = bool(is_permission)


if is_admin:
    access = True
elif is_active and is_permission and not is_admin:
    access = True
else:
    access = False

print(access)
