from pdf2image import convert_from_path
import os

def convert(img_name, filepath):
    pages = convert_from_path(filepath)
    img_path = os.path.join(os.getcwd(),'images')
    outfile = os.path.join(img_path,img_name[:-4]+'.jpg')
    for page in pages:
        page.save(outfile, 'JPEG')
    
    return outfile