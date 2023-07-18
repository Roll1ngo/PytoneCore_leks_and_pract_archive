import json

my_data = {"a":[1,2,3,4],
           "b":{1:1,2:2}}

byte_str = json.dumps(my_data)
unpacked = json.loads(byte_str)
print(unpacked)