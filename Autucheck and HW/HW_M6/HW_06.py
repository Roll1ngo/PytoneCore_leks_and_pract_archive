import shutil
import pathlib
from sys import argv
import os
IMAGES = ('.jpeg', '.png', '.svg','.jpg')
VIDEO = ('.avi', '.mp4', '.mov', '.mkv')
DOCS = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
MUSIC = ('.mp3', '.oog', '.wav', '.amr')
ARCHIVES = ('.zip', '.rar', '.gz','.tar')

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
)
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()



main_path = pathlib.Path(argv[1])

os.makedirs(f"{main_path}\Images",exist_ok=True)
os.makedirs(f"{main_path}\Videos", exist_ok=True)
os.makedirs(f"{main_path}\Docs", exist_ok=True)
os.makedirs(f"{main_path}\Archives", exist_ok=True)
os.makedirs(f"{main_path}\Music", exist_ok=True)
os.makedirs(f"{main_path}\Other", exist_ok=True)

def translate (name):
    trans_name = name.translate(TRANS)

    return trans_name







def get_pass_and_name(path):
    
    
    pass_key = {}
    
    for i in path.iterdir():
        if i.is_file():
            pass_key[i] = i.name
        elif i.is_dir():
            rec = get_pass_and_name(i)
            for k,v in rec.items():
                pass_key[k] = v
             
    return pass_key



# def remove_folder_end_archives(path):


    

#     for obj in path_name_dict.iterdir():
      
#         try:
#             if obj.is_dir():
#                os.rmdir(f"{obj}")
           
                
#         except OSError:
#            remove_folder_end_archives(obj)
           

#         return 


def main (main_path):
   
    path_name_dict = get_pass_and_name(main_path)


    for path, name in path_name_dict.items():
          
        
        if path.suffix in IMAGES:
            trans_name = translate(name)
            os.replace(fr"{path}", fr"{main_path}\Images\{trans_name}")
        elif path.suffix in VIDEO:
            trans_name = translate(name)
            os.replace(fr"{path}", fr"{main_path}\Videos\{trans_name}")
        elif path.suffix in MUSIC:
            trans_name = translate(name)
            os.replace(fr"{path}", fr"{main_path}\Music\{trans_name}")
        elif path.suffix in DOCS:
            trans_name = translate(name)
            os.replace(fr"{path}", fr"{main_path}\Docs\{trans_name}")
        elif path.suffix in ARCHIVES:
            trans_name = translate(name)
            format_suff =path.suffix.removeprefix(".")
            shutil.unpack_archive(fr"{path}", fr"{main_path}\Archives",format=f"{format_suff}")
        else:
            trans_name = translate(name)
            os.replace(fr"{path}", fr"{main_path}\Other\{name}")
    
    # remove_folder_end_archives(p)
    return 
main(main_path)








 












