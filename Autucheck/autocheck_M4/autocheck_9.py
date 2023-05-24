def is_valid_pin_codes(pin_codes):
    set_pin =set(pin_codes)
      
    
    for pin in set_pin:
      
       
        a= True if len(pin) == 4 and not len(pin)  ==0 else False
                 
        b = True if int(pin)/int(pin) ==1 else False
                       
        c = True if a and b else False

    
            
    return f"is_valid_pin_codes ({pin_codes}) == {c}"


 

   


print(is_valid_pin_codes(["1101", "9034", "0011", ]))     


    

  
        

             
    # print(pin)
           
    # pin = int(pin)
    # True if pin/1==pin else False
    # if True:
    #     set_pin.add(pin)
            
        #  a=  True if len(pin) == 4 else False
        #  print(a)


        # pin = int(pin)
        # b = True if pin/1 == pin else False



     

    
        

    


        
       
          






