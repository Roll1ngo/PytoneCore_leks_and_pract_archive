from re import search, findall,sub

# result = search("World$","Hello World")

# result = search("^World","Hello Worlds")

# result = search("Worlds*","Hello Worldsss")

# result = search("Worlds+","Hello Worlds")

# result = search("Worlds","Hello Worldsss")

# result = search("Worlds?","Hello Worlds World")
# result = search("Worlds{1,3}", "Hello Worlds")
# result = search("Worl(ds)? ", "Hello Worldsdsds")
# result = search("World(s|e|os)", "Hello Worldos")
# result = search("World(\d+|s|e)*", "Hello  World2022")
# result = search("World([a-z \d])*", "Hello  Worldgh1")
result = search(r"World[a-z]", "Hello  Worlda")
a = result.group()

print(a)
sub
