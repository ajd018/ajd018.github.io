import os
import shutil

with open('asdf.txt', 'r') as f:
    myNames = {line.strip() for line in f}

dir_src = r"\\cool\folder\bro"
dir_dst = r"\\cool\folder\bro"


for dirpath, dirs, files in os.walk(dir_src, topdown=True):
    for file in files:
        bn,ext = os.path.splitext(file)
        if ext == ".mxd" and any(s in file for s in myNames):
            shutil.copy( os.path.join(dirpath, file), dir_dst )
