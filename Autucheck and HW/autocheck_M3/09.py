def cost_delivery(*quantity, discount=0):
    """Функція виконує розрахунок вартості доставки.
     
      Перший параметр приймає у себе кількість замовлень одного клієнта,
        та розраховує вартість доставки з урахуванням наявності та розміру скидки 
        у другому параметрі."""



    
    sum = 5+(quantity[0] - 1)*2

    if  discount :
        sum -= sum * discount

    return sum


cost_delivery(2, 5, 8, 9, 6, 5, 2, 3, 2, 5, 6, 5)
print(cost_delivery.__doc__)
