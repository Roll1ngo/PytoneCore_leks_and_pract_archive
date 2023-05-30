grades = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}


def digit_ball(value):
    
        key_list = []

        for k, val in dict.items():

            if val == value:
                key_list.append(k)

        return key_list
