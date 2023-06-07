
     

    
def encrypt(b_obj,key):
    b_array = bytearray(b_obj)
    for index, byte in enumerate(b_array):
        new_simbol = byte+key
        if new_simbol>255:
            new_simbol -=255
        b_array[index] = new_simbol
    encrypted_password = bytes(b_array)
    return encrypted_password



def decrypt(b_obj, key):
    b_array = bytearray(b_obj)
    for index, byte in enumerate(b_array):
        new_simbol = byte-key
        if new_simbol <0:
            new_simbol += 255
        b_array[index] = new_simbol
        decrypted_password = bytes(b_array)
    return decrypted_password

if __name__ == "__main__":


    input_pass = input("Enter pass >>>")
    input_pass_bytes = input_pass.encode()
    


    enc_pass = encrypt(input_pass_bytes, 5)
    
    

    with open("password.txt", "wb") as file:
    
        file.write(enc_pass)
        
    with open("password.txt", "rb") as file:
        decr = file.read()
        print(decrypt(decr,5))
        
    
            
        
   

    
      

    
    


  