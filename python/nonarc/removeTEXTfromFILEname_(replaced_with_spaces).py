import os

folder = r'\\cool\folder\bro'

pathiter = (os.path.join(root, filename)
    for root, _, filenames in os.walk(folder)
    for filename in filenames
)
for path in pathiter:
    newname =  path.replace("_Legal", "")
    newname2 =  path.replace("_LEGAL 8.5 x 14", "")
    if newname != path:
        os.rename(path,newname)
    elif newname2 != path:
        os.rename(path,newname2)
