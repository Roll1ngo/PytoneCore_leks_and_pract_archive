def is_valid_pin_codes(pin_codes):
    
    if not pin_codes:

        return False


    if len(set(pin_codes)) != len(pin_codes):
       
        return False


    for pin in pin_codes:
    
            if len(pin) != 4:


               return False


            for i_2 in (pin):
                if  not 48 <=ord(i_2)<=57 and len(pin)>1: 
                     return False
              
    return True


print(is_valid_pin_codes(['1102', '1904', '0011']))
