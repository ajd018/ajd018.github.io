import arcpy, os
folderPath = r"C:\Users\ad39050\Desktop\testing\defquery"
for filename in os.listdir(folderPath):
    fullpath = os.path.join(folderPath, filename)
    if os.path.isfile(fullpath):
        basename, extension = os.path.splitext(fullpath)
        if extension.lower() == ".mxd":
            mxd = arcpy.mapping.MapDocument(fullpath)
            #loops through ALL DATAFRAMES
            for df in arcpy.mapping.ListDataFrames(mxd):  
                #only loops through layers in the group "STIP2018"
                for lyr in arcpy.mapping.ListLayers(mxd, "STIP2018", df)[0]:
                    if lyr.supports("DEFINITIONQUERY"):
                        #ternary statement that adds on. without this it will replace def query
                        lyr.definitionQuery = lyr.definitionQuery + (" OR " if lyr.definitionQuery else "") + 'County_No = 18'


            mxd.save()
            del mxd
           