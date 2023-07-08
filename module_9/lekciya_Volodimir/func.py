def best_func(param1:str):
    return param1.capitalize()


def simple_func(param1: int):
    return param1**2

def select_func(param):
    if param == int:
        return simple_func
    if param == str:
        return best_func
    return None


my_func_str= select_func(str)
my_func_int = select_func(int)
my_func_none = select_func([])
print(my_func_int.__name__)
