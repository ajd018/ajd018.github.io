import os
import sys
import arcpy

mxd_path = r'C:\Users\Desktop\test'

for dirpath, dirnames, filenames in os.walk(mxd_path):
    for filename in filenames:
        fullPath = os.path.join(dirpath, filename)
        basename, extension = os.path.splitext(filename)
        if extension.lower() == ".mxd":
            try:
                has_data_source = False
                mxd = arcpy.mapping.MapDocument(fullPath)
                for elm in arcpy.mapping.ListLayoutElements(mxd, 'TEXT_ELEMENT'):
                    elm.text = elm.text.replace('district 1 - this is some new text',
                                                'district 1 - this is some other text')

                    elm.text = elm.text.replace('district 2 - this is some new text',
                                                'district 2 - this is some other text')

                    elm.text = elm.text.replace('district 3 - this is some new text',
                                                'district 3 - this is some other text')

                    elm.text = elm.text.replace('district 4 - this is some new text',
                                                'district 4 - this is some other text')

                    elm.text = elm.text.replace('district 5 - this is some new text',
                                                'district 5 - this is some other text')

                    elm.text = elm.text.replace('district 6 - this is some new text',
                                                'district 6 - this is some other text')

                    elm.text = elm.text.replace('district 7 - this is some new text',
                                                'district 7 - this is some other text')

                    elm.text = elm.text.replace('district 8 - this is some new text',
                                                'district 8 - this is some other text')

                    elm.text = elm.text.replace('district 9 - this is some new text',
                                                'district 9 - this is some other text')

                    elm.text = elm.text.replace('district 10 - this is some new text',
                                                'district 10 - this is some other text')

                mxd.save()
                del mxd
            except IOError, e:
                for i in range(1):
                    print "Unable to copy file. %s" % e


