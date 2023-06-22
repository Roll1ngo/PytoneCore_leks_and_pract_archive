with open("text.bin", "wb") as file:
    print(file.write("Привіт Світ".encode("utf16")))



with open("text.bin", "rb") as file:
    data = file.read()
    print(len(data))
    # for i in data:
    #     print(i)