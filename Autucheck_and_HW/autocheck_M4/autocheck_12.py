from random import randint


def get_random_password():


    chr_list = []
    sim_list = []

    while len(chr_list) < 8:
        rand = randint(40, 126)
        chr_list.append(rand)

    for d in chr_list:
        a = chr(d)
        sim_list.append(a)
        new_pass = "".join(sim_list)

    return new_pass


def is_valid_password(password):
   
   
    apper_s = []
    lower_s = []
    number_s = []

    if len(password) != 8:
        return False

    for simbol in password:
        if 65 <= ord(simbol) <= 90:
            apper_s.append(simbol)
        elif 97 <= ord(simbol) <= 122:
            lower_s.append(simbol)
        elif 48 <= ord(simbol) <= 57:
            number_s.append(simbol)

    if not len(apper_s) or not len(lower_s) or not len(number_s):
        return False

    return True


def get_password():
    

    i=0
           
    while  i<100:
        a = get_random_password()
        b = is_valid_password(a)
                    
        if b == False:
            i += 1
            continue
        else:
            break
    
    return a

print(get_password())
    






