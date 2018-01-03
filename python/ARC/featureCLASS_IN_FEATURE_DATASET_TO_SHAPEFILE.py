import os

import arcpy

mxd_path = r'C:\folder\path\name'


for dirpath, dirnames, filenames in os.walk(mxd_path):
    for filename in filenames:
        fullPath = os.path.join(dirpath, filename)
        basename, extension = os.path.splitext(filename)
        if extension.lower() == ".mxd":
            has_data_source = False
            mxd = arcpy.mapping.MapDocument(fullPath)
            mxd = arcpy.mapping.MapDocument(fullPath)
            for lyr in arcpy.mapping.ListLayers(mxd):
                if lyr.supports("DATASOURCE"):
                    if lyr.dataSource == r"C:\folder\path\name\geodatabaseNAME.gdb\featureDataset\featureClass":
                        #PATH TO SHAPEFILE. THEN TYPE OF WORKSPACE. THEN SHAPEFILE NAME DO NOT PUT .SHP
                        lyr.replaceDataSource(r"C:\folder\path\name", 'SHAPEFILE_WORKSPACE', "shapefilename")


            mxd.save()
            del mxd
