def is_valid_password(password):
    apper_s = []
    lower_s =[]
    number_s = []

    if len(password) !=8:
        return False
    
    for simbol in password:
        if  65 <= ord(simbol) <= 90:
            apper_s.append(simbol)
        elif 97<=ord(simbol)<=122:
            lower_s.append(simbol)
        elif 48<=ord(simbol)<=57:
            number_s.append(simbol)
        else:
            continue
            
    if not len(apper_s) or not len(lower_s) or not len(number_s):
         return False
    
    return True

print(is_valid_password("AAAa1AAA"))
            
