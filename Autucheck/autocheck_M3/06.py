

def format_string(string, length):


    if len(string)>= length:
        format= string
    # elif len(string)<length:
    else:
        value_space= (length - len(string))//2
        format= (" " * value_space) + string
    return format

print(format_string("aaaaaaaaaaaaaaaaac",44))

