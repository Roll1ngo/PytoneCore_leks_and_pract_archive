def is_check_name(fullname, first_name):
    fullname = fullname.lower()
    first_name = first_name.lower()
    pref = fullname.removeprefix(first_name)
   
    if pref !=fullname:
        return True
    else:
        return False


print(is_check_name("Vladislav Bratus", "Vladilav"))
    