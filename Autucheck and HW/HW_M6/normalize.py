IMAGES = ('.jpeg', '.png', '.svg', '.jpg')
VIDEO = ('.avi', '.mp4', '.mov', '.mkv')
DOCS = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
MUSIC = ('.mp3', '.oog', '.wav', '.amr')
ARCHIVES = ('.zip', '.rar', '.gz', '.tar')

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ!\"@#$%&'()*+,-/:;<=>?-\\]^{|}"
TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",)

print(len(CYRILLIC_SYMBOLS),len(TRANSLATION))
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()



def normalize(name_object:str)->str:
    
    
    trans_name = name_object.translate(TRANS)
    
    return trans_name


f =normalize("Зроби t()e z@r@z.pdf")
print(f)





