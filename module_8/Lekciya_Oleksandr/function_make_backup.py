from datetime import datetime

def make_backup(data):
    current_time = datetime.now()
    target_day = datetime.strftime(current_time,"%H-%M-%S")
    with open (f"backup_{current_time.date()}_{target_day}.txt","w") as fh:
        fh.write(data)



if __name__ == "__main__":
    
    data = "slkdjfklsdjflksdjfkldsfjkldssjffkldsjf"

    make_backup(data)