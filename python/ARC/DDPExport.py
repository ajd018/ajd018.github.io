import arcpy
mxd = arcpy.mapping.MapDocument(r"\\cool\folder\bro\mapdoc.mxd")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    print "Exporting page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
    arcpy.mapping.ExportToPDF(mxd, r"\\cool\folder\bro" + str(pageNum) + ".pdf")
del mxd
