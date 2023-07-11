def game(terra,power):
    
    
    for i in terra:
        
        for i_2 in i:
            if i_2 <= power:
               power +=i_2
            else:
                break

    return power

print(game([[1, 1, 5, 10], [10,2],[1, 1, 1]], 1))






