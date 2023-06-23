from datetime import datetime

def randomizer_from_1_to_100 (s,f)-> int:
    
    while True:
        seed = datetime.now()
        micro_second = str(seed.microsecond)
        random_number = int(micro_second[0]+micro_second[1])
        
        if random_number in range(s,f):
            return random_number
            
        else:
            continue
    
if __name__ == "__main__":
    print(randomizer_from_1_to_100(10,20))
     