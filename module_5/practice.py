from re import sub

some_text = """ Уже вдеся́те майорить Приморський бульвар синьо-жовтими барвами, і вже вкотре ми збираємось у самому серці Одеси, щоб помилуватися показом автентичного вбрання, написати диктант просто неба, концентруючи  нашу енергію й демонструючи всім як свою єдність, так і свою любов до рідного міста та своєї країни. """
some_text = some_text.lower()
reg_exp = r'[^а-яА-Я0-9() і-]'
# print(some_text)
# print(len(some_text.split(" ")))
red_text = sub(reg_exp, "",some_text)


new = red_text.split(" ")
new = set(new)
words_dict = {}

for word in new:
    words_dict[word] = some_text.count(word)


words_dict_list = list(words_dict.items())



def sort_(element):
    return element[1]

words_dict_list.sort(key=sort_,reverse=True)

print(words_dict_list)












