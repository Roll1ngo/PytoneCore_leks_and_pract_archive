message = input("Enter a message:")
offset = int(input("Enter the offset:"))
encoded_message = ""

for lett in message:
    if ord(lett) >= ord("a"):
        pos = ord(lett) - ord("a")
        pos = (pos + offset) % 26
        encoded_message += chr(pos + ord("a"))

    elif ord("A") <= ord(lett) < ord("a"):
        pos = ord(lett) - ord("A")
        pos = (pos + offset) % 26
        encoded_message += chr(pos + ord("A"))
    else:
        encoded_message += lett

print(encoded_message)

