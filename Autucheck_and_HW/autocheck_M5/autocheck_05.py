def sanitize_phone_number(phone):
    san_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return san_phone


def get_phone_numbers_for_countries(list_phones):
    phones_dict = dict()
    ua_list = []
    jp_list = []
    tw_list = []
    sg_list = []
    
    
    for phone in list_phones:
        san_phone =sanitize_phone_number(phone)
        san_phone = str(san_phone)
                    

        if san_phone.startswith("81"):
            jp_list.append(san_phone)
            phones_dict["JP"] = jp_list
                       

        elif san_phone.startswith("65"):
            sg_list.append(san_phone)
            phones_dict["SG"] = sg_list
            
        elif san_phone.startswith("886"):
            tw_list.append(san_phone)
            phones_dict["TW"] = tw_list
            
        else: 
            ua_list.append(san_phone)
            phones_dict["UA"] = ua_list
               
    
    return phones_dict
        

        
       

print(get_phone_numbers_for_countries(["    +38(050)123-32-34",
                                           "     810503451234",
                                           "(650)8889900",
                                           "886050-111-22-22",
                                           "38050 111 22 11   "]))
