import arcpy
mxd = arcpy.mapping.MapDocument(r"<path>")

for lyr in arcpy.mapping.ListLayers(mxd, "Test")[0]:
    if lyr.supports("DEFINITIONQUERY"):
        lyr.definitionQuery = lyr.definitionQuery + (" OR " if lyr.definitionQuery else "") + '"county_num" = 20'


mxd.save()
del mxd
