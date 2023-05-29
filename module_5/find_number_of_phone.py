#0667584162
from re import search

some_text = "текст с номерами телефонов 89163325543, +79162341123, и вот так еще +7(916)2344433, нет это не реклама мтс 926 112 44 33, и не мегафона (926)123-22-11 и еще можно так 495 444-55-55"
list_text = some_text.split(" ")
pattern =r"^(\+)\d{10}"

for number in list_text:
    result = search(pattern,number)

    if result is None:
  
        continue

    else:

        print(f"Positive {result.group()}")

