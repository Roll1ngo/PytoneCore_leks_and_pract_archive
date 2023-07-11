def is_check_name(fullname, first_name):
    fullname = fullname.lower()
    first_name = first_name.lower()
    

    if fullname.startswith(first_name):
    
        return True
    
    return False


print(is_check_name("Vladislav Bratus", "Vladislav"))
