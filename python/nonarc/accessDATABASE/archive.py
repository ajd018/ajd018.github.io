import shutil
import datetime

now = datetime.datetime.now()
date=str(now.month)+'_'+str(now.day)+'_'+str(now.year)

new_folder = r"\\cool\folder\bro"
dest = new_folder + '/' + 'mapdocument' + str(date) + '.pdf'
shutil.copy(r'\\cool\folder\bro\mapdocument.pdf', dest)