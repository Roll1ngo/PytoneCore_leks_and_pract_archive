grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}


def lookup_key(dict, value):
    
    key_list = []
    
    for k, val in dict.items():
        
        if val == value:
            key_list.append(k)
            
    return key_list
       
       
          
    
print(lookup_key(grade, 5))
