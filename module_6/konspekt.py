# fh = open("test.txt","w")
# symbols_written = fh.write("hello!")
# print(symbols_written)
# fh.close()

fh = open("test.txt","w+")
fh.write("hello!")
# fh.close()

# fh = open("test.txt","r")
# all_file = fh.read()
# print(all_file)
# fh.close()


# first_two_simbols = fh.read(2)
# print(first_two_simbols)

# fh= open("test.txt", "w")
# fh.write("first line \nsecond line\nthird line")
# fh.close()

# fh = open("test.txt","r" )
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)

# fh.close()

# fh = open("test.txt","r")
# lines = fh.readlines()
# print(lines)
# fh.closed
# fh.seek(2)
# second = fh.read(2)
# print(second)
# fh.closed

position = fh.tell()
print(position)

fh.seek(1)
position = fh.tell()
print(position)
