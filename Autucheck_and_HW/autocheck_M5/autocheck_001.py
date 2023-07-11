def real_len(text):
    control_chars = ["\n", "\f", "\r", "\t", "\v"]
    new_list = []

    for el in text:
        if el not in control_chars:
            new_list.append(el)

    return len(new_list)


print(real_len('Alex\nKdfe23\t\f\v.\r'))
