import os
import shutil

with open('list.txt', 'r') as f:
    myNames = {line.strip() for line in f}

dir_src = r"\\cool\folder\bro"
dir_dst = r"\\cool\folder\bro"

exclude = set(['foldername2', 'foldername1', 'foldername3', 'foldername4', 'foldername5'])

for dirpath, dirs, files in os.walk(dir_src, topdown=True):
    dirs[:] = [d for d in dirs if d not in exclude]
    for file in files:
        bn,ext = os.path.splitext(file)
        if ext == ".pdf" and any(s in file for s in myNames):
            shutil.copy( os.path.join(dirpath, file), dir_dst )
