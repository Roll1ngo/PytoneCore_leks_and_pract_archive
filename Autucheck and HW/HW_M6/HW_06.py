import shutil
from pathlib import Path
from sys import argv
import os
IMAGES = ('jpeg', 'png', 'svg','jpg')
VIDEO = ('avi', 'mp4', 'mov', 'mkv')
DOCS = ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx')
MUSIC = ('mp3', 'oog', 'wav', 'amr')
ARCHIVES = ('zip', 'rar', 'gz','tar')

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")


TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

dont_touch_list =["archives","videos","images","docs","music","other"]

replace_simb = "!@#$%&'№()*+,-/.:;<=>?-\\]^{|}\""





def normalize(name_object: str) -> str:

    trans_name = name_object.translate(TRANS)
    
    
    for let in trans_name:
        
        if let in replace_simb:
            replace_simbol = trans_name.replace(let, "_")
            trans_name = replace_simb

    return trans_name

def get_path_list(path:Path):
    
    for item in path.glob("**/*"):
        if path.exists in
        

  
    return path_list



def remove_empty_folders(main_path:Path) -> None:
    
    for folders in os.listdir(main_path):
        fold = os.path.join(main_path, folders)
        
        if os.path.isdir(fold):
            remove_empty_folders(fold)
            
            if not os.listdir(fold):
                os.rmdir(fold)
    return




def main () -> None:

    main_path = Path(argv[1])
    
    path_list = get_path_list(main_path)
    
    # know_ex =open("know_ex_and_file_name","a")
    


    # for path, name in path_name_dict.items():
    #     name_without_suffix = name.removesuffix(path.suffix)
    #     trans_name = normalize(name_without_suffix) + path.suffix
    #     suffix_without_dot = path.suffix.removeprefix(".")
                                 
        
    #     if suffix_without_dot in IMAGES:
                                    
    #         know_ex.write(f"{suffix_without_dot}__________{name}\n")
            
    #         os.replace(fr"{path}", fr"{main_path}\images\{trans_name}")
        
       
    #     elif suffix_without_dot in VIDEO:
                        
    #         know_ex.write(f"{suffix_without_dot}__________{name}\n")
            
    #         os.replace(fr"{path}", fr"{main_path}\videos\{trans_name}")
        
        
    #     elif suffix_without_dot in MUSIC:
                       
    #         know_ex.write(f"{suffix_without_dot}__________{name}\n")
            
    #         os.replace(fr"{path}", fr"{main_path}\music\{trans_name}")
        
       
    #     elif suffix_without_dot in DOCS:
            
    #         know_ex.write(f"{suffix_without_dot}__________{name}\n")

    #         os.replace(fr"{path}", fr"{main_path}\docs\{trans_name}")
        
       
    #     elif suffix_without_dot in ARCHIVES:
           
    #         know_ex.write(f"{suffix_without_dot}__________{name}\n")

    #         format_suff =path.suffix.removeprefix(".")
            
    #         shutil.unpack_archive(fr"{path}", fr"{main_path}\Archives",format=f"{format_suff}")
            
    #         os.remove(f"{path}")
    #     else:
            
    #         os.replace(fr"{path}", fr"{main_path}\other\{name}")
    #         unknow_ex = open("unknow_ext_and_file_name.txt", "a")
    #         unknow_ex.write(f"{suffix_without_dot}__________{name}\n")

   
    # remove_empty_folders(main_path)
    
    
    # unknow_ex.close()
    # # path_unknow_ex = os.path.join(os.getcwd(), "unknow_ext_and_file_name.txt")
    # # os.replace(path_unknow_ex,main_path)
    
    
    # know_ex.close()
    # # path_know_ex = os.path.join(os.getcwd(), "know_ex_and_file_name")
    # # os.replace(path_know_ex, main_path)
    # #
      
    # return 

if __name__ == "__main__":
    print(main())









 












