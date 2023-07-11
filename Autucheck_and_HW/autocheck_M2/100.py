num = None
sum = 0
while True:  
    num = int(input("Enter integer (0 for output): ")) 
    if num:
                   
     sum += num
     print(sum)
    if num==".":
       print(sum)
       break
