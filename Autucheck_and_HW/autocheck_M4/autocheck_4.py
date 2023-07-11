grade ={"F":1, "FX":2, "E":3, "D":3, "C":4, "B":5, "A":5}
description = {"F":"Unsatisfactorily", "FX":"Unsatisfactorily", "E":"Enough", "D":"Satisfactorily", "C":"Good", "B":"Very good", "A":"Perfectly"}

def get_grade(key):
    result = grade.get(key)
    return result

def get_description(key):
    result = description.get(key)
    return result




print(get_grade("FX"))
print(get_description("F"))
