import re


def find_all_phones(text):
    # new_res =()
    regex = r"\+\d{3}\(\d{2}\)\d{3}-(?:\d{2}\-\d{2}|\d{1}\-\d{3})"
    
    

    # for phone in finds_number:
    #     new_res.append(phone[0])
    # return new_res
    return re.findall(regex, text)


print(find_all_phones(
    'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'))

