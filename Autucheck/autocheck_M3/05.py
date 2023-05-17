def get_fullname(first_name, last_name, middle_name=None ):
    a = f"{first_name} {middle_name} {last_name}"

    if middle_name==None:
        a =f"{first_name} {last_name}"
    return a
    

print(get_fullname("A","B"))
