def sanitize_phone_number(phone):


   
    clean_number = phone.strip()\
                        .replace("(", "")\
                        .replace("-", "")\
                        .replace(")","")\
                        .replace(" ","")\
                        .replace("+","")
    
    return clean_number
    


print(sanitize_phone_number("    +38(050)123-32-34"))
                             
