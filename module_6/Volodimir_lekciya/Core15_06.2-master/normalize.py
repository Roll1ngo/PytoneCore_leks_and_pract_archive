IMAGES = ('.jpeg', '.png', '.svg', '.jpg')
VIDEO = ('.avi', '.mp4', '.mov', '.mkv')
DOCS = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
MUSIC = ('.mp3', '.oog', '.wav', '.amr')
ARCHIVES = ('.zip', '.rar', '.gz', '.tar')

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
replace_simb = "@#$%&'№()*+,-/.:;<=>?-\\]^{|}"

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()



def normalize(name_object:str)->str:
       
    trans_name = name_object.translate(TRANS)
       
    for symbol in trans_name:
        if symbol in replace_simb:
                      
            replace_name=trans_name.replace(symbol,"_")
            trans_name =replace_name
   
    return trans_name
    
if __name__ =="__main__":


    f =normalize("()Зроби це зараз )")
    print(f)





