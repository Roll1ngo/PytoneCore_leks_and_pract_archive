from Functions_work_with_text.HW_06 import normalize as norm
from pathlib import Path

name = "Я у порядку"
trans_name = norm(name)
print(trans_name)

# path = Path("E:\Junk")
# path_list = get_pass_and_name(path)
# print(path_list)
# from utility.dummy.function import nice_function
# from utility.useful.function import not_bad

# nice_function()
# not_bad()

# from utility import *

# nice_function()
# not_bad()
