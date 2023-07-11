def formatted_numbers():
    result = []
    f_head = "|{:^10}|{:^10}|{:^10}|".format("decimal","hex","binary")
    result.append(f_head)
    
    for i in range(16):
        f_table= "|{n:<10d}|{n:^10x}|{n:>10b}|".format(n=i)
        result.append(f_table)
    return result
                 
    

print(formatted_numbers())