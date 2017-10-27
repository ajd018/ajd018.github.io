import arcpy, os
folderPath = r"\\cool\folder\bro"
for filename in os.listdir(folderPath):
    fullpath = os.path.join(folderPath, filename)
    if os.path.isfile(fullpath):
        basename, extension = os.path.splitext(fullpath)
        if extension.lower() == ".mxd":
            mxd = arcpy.mapping.MapDocument(fullpath)
            arcpy.mapping.ExportToPDF(mxd, basename + '.pdf', resolution = 125)
