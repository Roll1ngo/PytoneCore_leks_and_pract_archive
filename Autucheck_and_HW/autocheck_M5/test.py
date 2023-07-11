import re


def find_all_emails(text):
   res = list()
   regexp = r"https?://[\w]*\.\w{2,}[\w\.]+"
   matches =re.finditer(regexp, text)
   for match in matches:
      res.append(match.group())
   return res
      

print(find_all_emails("The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com"
                      ))
