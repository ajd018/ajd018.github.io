import arcpy
from arcpy import env


env.workspace = r"\\cool\folder\bro"
for mxdname in arcpy.ListFiles("*.mxd"):
    print mxdname
    mxd = arcpy.mapping.MapDocument(r"\\cool\folder\bro\\" + mxdname)
    for TextElement in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "TextElement1"):
        if TextElement.name == "TextElement1":
            TextElement.text = "test"
    mxd.save()
del mxd
