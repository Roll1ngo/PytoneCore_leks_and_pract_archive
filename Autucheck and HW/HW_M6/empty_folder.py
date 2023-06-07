import pathlib
import os
folder_path = "E:\Empty"


def del_empty_dirs(adress: str) -> None:
    for dirs in os.listdir(adress):
        dir = os.path.join(adress, dirs)
        if os.path.isdir(dir):
            del_empty_dirs(dir)
            if not os.listdir(dir):
                os.rmdir(dir)
del_empty_dirs(folder_path)
