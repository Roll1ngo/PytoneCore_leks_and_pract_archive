
from re import sub

def is_spam_words(text, spam_words, space_around=False):
    reg = r'[^а-яА-Я0-9 ]'
    text = sub(reg, "", text)

    for spam_word in spam_words:

        if space_around == False:
            if text.find(spam_word) != -1:
                return True

        elif space_around:

            split_text = text.split(" ")

            for word in split_text:

                if word == spam_word:
                    return True

    return False


print(is_spam_words('Молох бог ужасен.', ["лох"]))
