from functools import wraps
from datetime import datetime


def simple_decorator(func):

    @wraps(func)
    def simple_wrapper(*args, **kwargs):
        date = datetime.now()
        print(f"Before{date} ")   
        result = func(*args, **kwargs)
        print(f"After {date} ")   
                    
    
        return (result)
    return simple_wrapper


@simple_decorator
def mult(x,y):
    print(x*y)
    return x*y

mult(5,7)



