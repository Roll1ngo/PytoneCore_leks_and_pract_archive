def prepare_data(some_list):
    changed_list = sorted(some_list)
    changed_list.pop (0)
    changed_list.pop(-1)
    result = changed_list
    
    return result
   
print(prepare_data([1,-3,4,100,0,-5,10,1,1]))
