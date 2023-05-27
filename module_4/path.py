from pathlib import Path

p = Path('C:\Test_Path/Bandicam')
# print(p.iterdir())

for i in p.iterdir():
    print(i.suffix)
    