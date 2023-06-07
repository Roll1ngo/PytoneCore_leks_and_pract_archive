def is_valid_pin_codes(pin_codes):

    if len(pin_codes)<1:

        return False

    if len(set(pin_codes)) != len(pin_codes):

        return False

    for pin in pin_codes:

           if len(pin) != 4:

               return False

           for pin_2 in (pin):
                if  not 48 <= ord(pin_2)<=57 : 
                    return False

    return True



print(is_valid_pin_codes(['1104', '1294', '0011']))
