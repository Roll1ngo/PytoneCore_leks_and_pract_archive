import re


def find_all_words(text, word):

    
    find_all = re.findall(r"[p]\w{4}[n]", text, flags=re.IGNORECASE)

    return find_all


print(find_all_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', 'Python'))



