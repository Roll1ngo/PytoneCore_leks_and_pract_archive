def format_ingredients(ingrids):
   
   result = ""
   counter = 0
   for i in ingrids:
        
        if counter == 0:
           result = f"{ingrids[0]}"
           
        elif len(ingrids) - 1 == counter:
           result += f" and {ingrids[counter]}"
       
             
        elif len(ingrids) > counter:
          result += f", {ingrids[counter]}"

        else:
           break
       
        counter += 1


   return result


a = format_ingredients(["2 eggs", " 1 liter sugar", "1 tsp salt", "vinegar",])
print(a)
    
