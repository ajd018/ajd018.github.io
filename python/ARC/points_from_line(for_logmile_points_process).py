import arcpy

arcpy.env.workspace = r"\\cool\folder\bro\Geodatabase.gdb"

points = []
for row in arcpy.da.SearchCursor(r'\\cool\folder\bro\Geodatabase.gdb\featurenameline', ["SHAPE@"]): # change this to your source line layer
    length = int(row[0].length)
    for i in xrange(0, length + 10, 10): # assuming units are in meters for feature spatial reference
        point = row[0].positionAlongLine(i)
        points.append(point)
arcpy.CopyFeatures_management(points, r'\\cool\folder\bro\Geodatabase.gdb\featurenamepoints')
