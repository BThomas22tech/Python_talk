import os
import platform
import pathlib

myfolder = pathlib.Path.cwd()
print("myfolder",myfolder)

myfile = myfolder/'files'/'example.txt'
print(myfile)

if platform.system() == "Windows": os.system(f"explorer {myfile}")
elif platform.system() == "Darwin": os.system(f"open {myfile}")
else: os.system(f"xdg-open {myfile}")

