import os

import arcpy

with open('LIST.txt', 'r') as f:
    myNames = {line.strip() for line in f}

mxd_path = r'\\cool\folder\bro'

dir_dst = r"\\cool\folder\bro"


for dirpath, dirnames, filenames in os.walk(mxd_path):
    for filename in filenames:
        fullPath = os.path.join(dirpath, filename)
        basename, extension = os.path.splitext(filename)
        if extension.lower() == ".mxd" and any(s in filename for s in myNames):
            has_data_source = False
            mxd = arcpy.mapping.MapDocument(fullPath)

            arcpy.mapping.ExportToPDF(mxd, dir_dst + "\\" + basename + '.pdf', resolution = 125)