
import os

import arcpy

mxd_path = r'\\cool\folder\bro'


for dirpath, dirnames, filenames in os.walk(mxd_path):
    for filename in filenames:
        fullPath = os.path.join(dirpath, filename)
        basename, extension = os.path.splitext(filename)
        if extension.lower() == ".mxd":
            has_data_source = False
            mxd = arcpy.mapping.MapDocument(fullPath)
            arcpy.mapping.ExportToJPEG(mxd, basename + '.jpg', resolution=1000)