import arcpy
mxd = arcpy.mapping.MapDocument(r"\\cool\folder\bro\basemap.mxd")
find_word = 'this'
replace_word = 'that'

for elm in arcpy.mapping.ListLayoutElements(mxd, 'TEXT_ELEMENT'):
        if find_word in elm.text:
            elm.text = elm.text.replace(find_word, replace_word)

mxd.save()
del mxd