from re import sub

def sanitize_phone_number(phone):
    
    regular = r"[^0-9]"

    result=( sub(regular,"",phone))
    
    return result


print(sanitize_phone_number("    +38(050)123-32-34",))
