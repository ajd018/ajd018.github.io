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
            mxd = arcpy.mapping.MapDocument(fullPath)
            for lyr in arcpy.mapping.ListLayers(mxd):
                if lyr.supports("DATASOURCE"):
                    if lyr.dataSource == r"\\cool\folder\bro\shapefile.shp":
                        lyr.replaceDataSource(r"\\cool\folder\bro\geodatabase.gdb", "dataset", "feature4")

                    if lyr.dataSource == r"\\cool\folder\bro\shapefile2.shp":
                        lyr.replaceDataSource(r"\\cool\folder\bro\geodatabase.gdb", "dataset", "feature5")

                    if lyr.dataSource == r"\\cool\folder\bro\shapefile3.shp":
                        lyr.replaceDataSource(r"\\cool\folder\bro\geodatabase.gdb", "dataset", "feature6")

            mxd.save()
            del mxd
