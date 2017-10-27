import arcpy, os
from arcpy import env
mxd = arcpy.mapping.MapDocument(r"\\cool\folder\bro\TESTTEST.mxd")
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("DATASOURCE"):
        if lyr.dataSource == r"\\cool\folder\bro\shapefile.shp":
                        lyr.replaceDataSource(r"\\cool\folder\bro\geodatabase.gdb", "dataset", "feature")

mxd.save()
del mxd