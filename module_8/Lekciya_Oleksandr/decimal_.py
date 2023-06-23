from decimal import Decimal, getcontext
a = 0.1 + 0.2
print(round(a,10)==0.3)

getcontext().prec = 2
print(Decimal(0.1)+Decimal(0.2)==0.3)
