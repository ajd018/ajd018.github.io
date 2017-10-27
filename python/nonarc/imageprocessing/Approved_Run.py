import os, shutil, datetime

#STEP ONE: COPY PDFS

tempmaps = r'\\cool\folder\bro\TEMPmaps'
web = r'\\WEB\wwwroot\program_mgmt\gis\webmaps'
current = r'\\cool\folder\bro\currentstaticfolder'
DOCS = r'\\cool\folder\bro\pdf'
DIR = r'\\cool\folder\bro\images'

for fname in os.listdir(tempmaps):
    if fname.lower().endswith('.pdf'):
        shutil.copy(os.path.join(tempmaps, fname), os.path.join(web, fname))
        shutil.copy(os.path.join(tempmaps, fname), os.path.join(current, fname))

#STEP TWO: date and time folder

today = datetime.date.today()
todaystr = today.isoformat()
os.makedirs(today.strftime(r'\\cool\folder\bro' "/%Y" + "_" "%m"))

for fname in os.listdir(DOCS):
    if fname.lower().endswith('.pdf'):
        shutil.copy(os.path.join(DOCS, fname), os.path.join(today.strftime(r'\\cool\folder\bro' "/%Y" + "_" "%m"), fname))

#STEP THREE: delete



for the_file in os.listdir(DIR):
    file_path = os.path.join(DIR, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

#STEP FOUR: delete

for the_file in os.listdir(DOCS):
    file_path = os.path.join(DOCS, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)
