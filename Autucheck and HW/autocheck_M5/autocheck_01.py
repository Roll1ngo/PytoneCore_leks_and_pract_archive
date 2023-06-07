from re import sub
def real_len(text):
    reg = r'[^a-zA-z0-9. ]'
    new_text = sub(reg, "",text)

    return len(new_text)


print(real_len('Alex\nKdfe23\t\f\v.\r'))




# chars = ["\n", "\f", "/r", "\t", "\v"]
# a = "Alex\nKdfe23\t\f\v.\r"
# b = a.replace(chars,"")
# print(b)



