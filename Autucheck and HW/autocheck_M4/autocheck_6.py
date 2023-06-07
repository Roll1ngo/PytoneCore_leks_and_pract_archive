def split_list(grade:int):
    grade = int(grade)
    average = 0
    aver_ball = []
    high_ball = []
    
    for ball in grade:
        average += ball /len(grade)

              

    for ball in grade:   
        if ball<= average:
            aver_ball.append(ball)
            # tuple_aver = tuple(aver_ball)
        else:
            high_ball.append(ball)
            # tuple_high = tuple(high_ball)

    
    return aver_ball, high_ball

  
    


print(split_list([1,4,8,16,3,8]))
