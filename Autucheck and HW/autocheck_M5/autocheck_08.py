grades = {"F": 1,
          "FX": 2,
          "E": 3,
          "D": 3,
          "C": 4,
          "B": 5,
          "A": 5}


def formatted_grades(students):
    result = []
    i = 1

    for name, ball in students.items():
        f = "{:>4}|{:<10}|{:^5}|{:^5}".format(
            i, name, ball, grades.get(ball))
        result.append(f)
        i += 1
    return result


print(formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}))
