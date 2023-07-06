some_str = "aaFGffHBVV       GFFffj "
save_list = []

for i in filter(lambda x:x.lower(), some_str):
    save_list.append(i)
print(save_list)