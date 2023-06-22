with open("text.txt") as file:
    while True:
        symbol = file.read(1)
        if not symbol:
            break
        if symbol == "\n":
            print("")
            continue
        print(symbol)

# with open("text.txt") as file:
#     data = file.read()
#     for i in data:
#         print(ord(i))