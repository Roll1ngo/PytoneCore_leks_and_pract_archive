# with open("text.txt", "w") as f:
#     data = f.write("Hello")
#     print(data)

file = open("text.txt", "w")

data = file.write("Hello World")
print(data)

file.close()