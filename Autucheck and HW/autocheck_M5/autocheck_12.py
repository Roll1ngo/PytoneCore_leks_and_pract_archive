import re

def replac_spam_words(text, spam_words):

         
    for spam in spam_words:
        len_spam = "*"*len(spam)
        find_spam =re.sub(spam,len_spam, text, flags=re.IGNORECASE)
        text=find_spam
          
        
    return text


print(replac_spam_words("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ", ['Python',"began"]))

        
        
        
        
        
