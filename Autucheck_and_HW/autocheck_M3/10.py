def factorial(n):


    if n<2:
        return 1
    else:
        return n* factorial(n-1)
    
    
f=factorial(5)
print(f)


def number_of_groups(n,k):
    
    
    (C)=int(factorial(n)/(factorial(n-k) * factorial(k)))
    return C

print(number_of_groups(50,7))



