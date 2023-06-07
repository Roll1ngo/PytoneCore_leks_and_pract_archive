def amount_payment(payment):
    print(type(payment))
    sum = 0
    for pay in payment:
        if pay > 0:
            sum +=pay
    return sum


total_payments = amount_payment([5, 10, -6, -12])
print(total_payments)






