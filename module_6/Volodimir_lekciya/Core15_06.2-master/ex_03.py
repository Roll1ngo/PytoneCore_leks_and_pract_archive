text = "Hello"
byte_text = b"Hello"

print(text)
print(byte_text)

for i in text:
    print(i)
    
for i in byte_text:
    print(hex(i))

print(text == byte_text.decode())