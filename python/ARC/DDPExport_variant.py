import arcpy
mxd = arcpy.mapping.MapDocument(r"\\cool\folder\bro\mapdoc.mxd")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    arcpy.AddMessage("Exporting PDF Map " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount))
    pageName = mxd.dataDrivenPages.pageRow.county_nam
    arcpy.mapping.ExportToPDF(mxd, r"\\cool\folder\bro" + pageName + ".pdf")
