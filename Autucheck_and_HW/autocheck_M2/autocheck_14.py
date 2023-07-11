pool = 1000
quantity = input("Enter the number of mailings: ")

try:
    chunk = pool / quantity
    quantity = str()

except:
    print("Enter integer")
finally:
    print("Thats all")
