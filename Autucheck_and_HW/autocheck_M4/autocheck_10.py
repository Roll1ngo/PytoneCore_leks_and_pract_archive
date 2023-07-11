from random import randint

def get_random_password():
  
  
    chr_list= []
    sim_list= []
    
    while len(chr_list)<8:
        rand = randint(40,126)
        chr_list.append(rand)

    for  d in chr_list:
        a = chr(d)
        sim_list.append(a)
        new_pass = "".join(sim_list)

    return new_pass
    




