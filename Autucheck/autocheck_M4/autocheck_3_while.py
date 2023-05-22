def format_ingredients(ingrids):
    result = ""
    
    if len(ingrids)>1:
        result = f"{ingrids[0]}"
        counter=1
        print(result)
        
        while counter<len(ingrids):
            if counter == len(ingrids) -1:
                result+=f" and {ingrids[counter]}"
            else:
                result += f", {ingrids[counter]}"
                print(result)

            counter+=1
    return result
      

    
a = format_ingredients(["2 eggs"," 1 liter sugar", "1 tsp salt","vinegar"])
print(a)