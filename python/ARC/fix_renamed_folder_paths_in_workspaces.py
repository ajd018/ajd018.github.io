import os
import arcpy

mxd_path = r'C:\Users\ad39050\Desktop\yeanice'

for dirpath, dirnames, filenames in os.walk(mxd_path):
    for filename in filenames:
        fullPath = os.path.join(dirpath, filename)
        basename, extension = os.path.splitext(filename)
        if extension.lower() == ".mxd":
            has_data_source = False
            mxd = arcpy.mapping.MapDocument(fullPath)
            mxd.findAndReplaceWorkspacePaths(r"C:\Users\ad39050\Desktop\anothername",
                                             r"C:\Users\ad39050\Desktop\yeanice")
            mxd.save()
            del mxd
