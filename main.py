from detect_and_predict import detect
from pdf2img import convert
import os
import cv2
import numpy as np
import shutil
# importing helper functions

invoices_dir = os.path.join(os.getcwd(),'invoices')

# for inv in os.listdir(invoices_dir):
    
#     if inv.endswith('.pdf'):
#         conv = convert(inv, os.path.join(invoices_dir,inv))
    
#     elif inv.endswith('.jpg') or inv.endswith('.png'):
#         src_path = os.path.join(invoices_dir, inv)
#         dst_path = os.path.join(os.getcwd(),'images',inv)
#         shutil.copy(src_path, dst_path)

images_dir = os.path.join(os.getcwd(),'images')

for img in os.listdir(images_dir):
    img_path = os.path.join(images_dir,img)
    detect(img, img_path)
        