def cost_delivery(*quantity, discount = 0):
    sum = 5+(quantity[0] -1)*2
    

    if discount:
        sum -=sum *discount
    
    return sum

cost_delivery(2,5,8,9,6,5,2,3,2,5,6,5)



