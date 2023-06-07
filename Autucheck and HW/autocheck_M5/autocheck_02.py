articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    
    result = []

    if letter_case == False:
        key_lower = key.lower()

        
        for i in articles_dict:

            for find_value in i.values():

                find_value = str(find_value)
                lower_string = find_value.lower()
                            
                if lower_string.find(key_lower) == -1:
                    continue

                else:
                    result.append(i)

    elif letter_case:
        for i in articles_dict:

            for find_value in i.values():

                find_value = str(find_value)
               
                if find_value.find(key) == -1:
                    continue

                else:
                    result.append(i)
    
    
    return result

print(find_articles("ocean"))
