# a=[ 4,5,2,"asd",4,5,2,3,]
# print(a,type(a), len(a))
# b=set(a)
# print(b,type(b), len(b))
first_people = "Elone Musk"
second_people = " Steve Jobs"
first_set = set("Ellon Musk")
second_set = set("Steve Jobs")

# print(first_set, second_set)

print(first_set.difference(second_set))
print(first_set& second_set)
print(first_set | second_set)
print(first_set^ second_set)