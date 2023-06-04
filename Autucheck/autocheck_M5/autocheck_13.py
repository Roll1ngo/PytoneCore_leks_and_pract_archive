import re

def find_all_emails(text):
    return re.findall(r"[A-Za-z][\w\.]{1,}@\w+\.\w{2,}",text)


print(find_all_emails(
    "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"))
