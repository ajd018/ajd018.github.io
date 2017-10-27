import os
import shutil

with open('LIST.txt', 'r') as f:
    myNames = {line.strip() for line in f}

dir_src = r"\\cool\folder\bro"
dir_dst = r"\\cool\folder\bro\newlocation"

for dirpath, dirs, files in os.walk(dir_src):
    for file in files:
        bn,ext = os.path.splitext(file)
        if ext == ".pdf" and any(s in file for s in myNames):
            shutil.copy( os.path.join(dirpath, file), dir_dst )