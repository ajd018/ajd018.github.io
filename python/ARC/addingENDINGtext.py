import os
import arcpy

mxd_path = r'C:\Users\Desktop\test'

for dirpath, dirnames, filenames in os.walk(mxd_path):
    for filename in filenames:
        fullPath = os.path.join(dirpath, filename)
        basename, extension = os.path.splitext(filename)
        if extension.lower() == ".mxd":
            has_data_source = False
            mxd = arcpy.mapping.MapDocument(fullPath)
            for elm in arcpy.mapping.ListLayoutElements(mxd, 'TEXT_ELEMENT'):
                elm.text = "District {0} - Additional text goes here".format(elm.text)

            mxd.save()
            del mxd
