from fpdf import FPDF
from PIL import Image, ImageChops, ImageDraw
import glob
import os, sys
from PyPDF2 import PdfFileReader, PdfFileMerger
import shutil

#STEP ONE: jpeg to pdf conversion

image_directory = r'\\cool\folder\bro\images'
DEST_DIR = r'\\cool\folder\bro\pdf'
DIR = r'\\cool\folder\bro\imagefolder'
temp = r'\\\cool\folder\bro\TEMPmaps'

extensions = ('*.jpg','*.png','*.gif')

imagelist=[]
for ext in extensions:
    imagelist.extend(glob.glob(os.path.join(image_directory,ext)))

for imagePath in imagelist:

    cover = Image.open(imagePath)
    width, height = cover.size

    if height > width:
        pdf = FPDF(unit = "pt", format = "legal")
        pdf.add_page()
        pdf.image(imagePath, 0, 0, 600)
        destination = os.path.splitext(imagePath)[0]
        pdf.output(destination + ".pdf", "F")

    if width > height:
        pdf = FPDF("L", unit = "pt", format = "legal")
        pdf.add_page()
        pdf.image(imagePath, 0, 0, 0, 600)
        destination = os.path.splitext(imagePath)[0]
        pdf.output(destination + ".pdf", "F")
    cover.close()

# STEP TWO: jpeg to pdf conversion

for the_file in os.listdir(DEST_DIR):
    file_path = os.path.join(DEST_DIR, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

for fname in os.listdir(image_directory):
    if fname.lower().endswith('.pdf'):
        shutil.move(os.path.join(image_directory, fname), os.path.join(DEST_DIR, fname))

# STEP THREE: rename files in pdf

pathiter = (os.path.join(root, filename)
    for root, _, filenames in os.walk(DEST_DIR)
    for filename in filenames
)
for path in pathiter:
    newname =  path.replace("_Legal", "")
    newname2 =  path.replace("_LEGAL 8.5 x 14", "")
    if newname != path:
        os.rename(path,newname)
    if newname2 != path:
        os.rename(path,newname2)

# STEP FOUR: rename files in image

pathiter = (os.path.join(root, filename)
    for root, _, filenames in os.walk(image_directory)
    for filename in filenames
)
for path in pathiter:
    newname =  path.replace("_Legal", "")
    newname2 =  path.replace("_LEGAL 8.5 x 14", "")
    if newname != path:
        os.rename(path,newname)
    if newname2 != path:
        os.rename(path,newname2)

# STEP FIVE: delete old jpgs

for the_file in os.listdir(DIR):
    file_path = os.path.join(DIR, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)

    except Exception as e:
        print(e)

# STEP SIX: COPY JPGS TO UPDATE FOLDER

for fname in os.listdir(image_directory):
    if fname.lower().endswith('.jpg'):
        shutil.copy(os.path.join(image_directory, fname), os.path.join(DIR, fname))

# STEP SEVEN: first jpg trim

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

path = r"\\cool\folder\bro\imagefolder\\"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item) and item[len(item)-4:] == ".jpg":
                im = Image.open(path+item)
                f, e = os.path.splitext(path+item)
                imResize = trim(im)
                imResize = trim(im)
                try:
                    imResize.save(f + '.jpg', 'JPEG', quality=95)
                except:
                    pass
resize()

# STEP EIGHT: adding orientation

directory = r"\\cool\folder\bro\imagefolder\\"

for fn in os.listdir(directory):
    try:
        if os.path.isfile(directory + fn) and fn[len(fn) - 4:] == ".jpg":
            img = Image.open(directory + fn)
            width, height = img.size

            if fn == "landscapemap.jpg":
                img.save(directory + fn[:len(fn) - 4] + "_Landscape.jpg")
                img2 = img.rotate(-90, expand=True)
                img2.save(directory + fn)
            elif height > width:
                img2 = img.rotate(90, expand=True)
                img2.save(directory + fn[:len(fn) - 4] + "_Landscape.jpg")
    except:
        pass

# STEP NINE: white box placement

for fn in os.listdir(directory):
    if os.path.isfile(directory + fn) and fn[len(fn) - 4:] == ".jpg":
        img = Image.open(directory + fn)
        draw = ImageDraw.Draw(img)
        width, height = img.size

        if height > width:
            draw.rectangle(((0, height - 1500), (50, height)), fill="white", outline="white")
        else:
            draw.rectangle(((width - 1500, height - 50), (width, height)), fill="white", outline="white")

        try:
            img.save(directory + fn, quality=95)
        except:
            pass

# STEP TEN: second trim

def trim(im, colorToCrop=None):
    if colorToCrop is None:
        colorToCrop = im.getpixel((0, 0))

    bg = Image.new(im.mode, im.size, colorToCrop)
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()

    if bbox:
        return im.crop(bbox)

dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item) and item[len(item)-4:] == ".jpg":

                im = Image.open(path+item)
                f, e = os.path.splitext(path+item)
                imResize = trim(im, (255, 255, 255))
                width, height = imResize.size
                imResize = imResize.resize((width // 2, height // 2), Image.LANCZOS)
                try:
                    imResize.save(f + '.jpg', 'JPEG', quality=70)
                except:
                    pass
resize()

# STEP ELEVEN: merging pdfs into all

try:
    os.remove(r"\\cool\folder\bro\pdf\combinedmap.pdf")
except OSError:
    pass

pdf_files = [f for f in os.listdir(DEST_DIR) if f.endswith("pdf")]
merger = PdfFileMerger()

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(DEST_DIR, filename), "rb"))

merger.write(os.path.join(DEST_DIR, "combinedmap.pdf"))

# STEP TWELVE: moving pdfs to temp folder

orig_stdout = sys.stdout
f = open(r'\\cool\folder\bro\NOCOPY.txt', 'w')
sys.stdout = f

for fname in os.listdir(DEST_DIR):
    if fname.lower().endswith('.pdf'):
        try:
            shutil.copy(os.path.join(DEST_DIR, fname), os.path.join(temp, fname))
        except IOError, e:
            for i in range(1):
                print "Unable to copy file. %s" % e
sys.stdout = orig_stdout
f.close()
