import pickle

data = {"a":[1,2,3,4],
        "b":"Hello"}

byte_str = pickle.dumps(data)
print(byte_str)

unpacked_data = pickle.loads(byte_str)

print(data == unpacked_data)

with open ("data.bin","wb") as file:
    pickle.dump(data,file)

with open ("data.bin","rb") as file:
    un =pickle.load(file)

print(un)