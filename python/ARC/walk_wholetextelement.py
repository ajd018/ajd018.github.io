import os
import sys
import arcpy

mxd_path = r'\\cool\folder\bro'

#orig_stdout = sys.stdout
#f = open(r'\\cool\folder\bro\NOCOPY.txt', 'w')
#sys.stdout = f

for dirpath, dirnames, filenames in os.walk(mxd_path):
    for filename in filenames:
        fullPath = os.path.join(dirpath, filename)
        basename, extension = os.path.splitext(filename)
        if extension.lower() == ".mxd":
            try:
                has_data_source = False
                mxd = arcpy.mapping.MapDocument(fullPath)
                for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
                    if elm.text == "this text":
                        elm.text = "that text"
                mxd.save()
                del mxd
            except IOError, e:
                for i in range(1):
                    print "Unable to copy file. %s" % e

#sys.stdout = orig_stdout
#f.close()


