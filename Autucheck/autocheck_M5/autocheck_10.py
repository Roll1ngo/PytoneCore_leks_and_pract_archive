import re

def find_word(text,word):
    dict_search = dict()
    search_text =re.search(word,text)
    bull_search = True if search_text else False
    
    
    if bull_search:   
        
        span = re.Match.span(search_text)
        dict_search["result"] = bull_search
        dict_search["first_index"] = span[0]
        dict_search["last_index"] = span[1]
        dict_search["search_string"] = re.Match.group(search_text)
        dict_search["string"] = text
       

    elif bull_search==False:
         dict_search["result"] = bull_search
         dict_search["first_index"] = None
         dict_search["last_index"] = None
         dict_search["search_string"] =word
         dict_search["string"] = text
    
    
    

    return dict_search


print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.","Python"))
