import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Staff201\AppData\Local\Tesseract-OCR\tesseract.exe'
text_dir = os.path.join(os.getcwd(),'converted')

def detect(img_name, imgpath, rect_kernel=(9,3)):
    img = cv2.imread(imgpath)
    rgb = cv2.pyrDown(img)
    img = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#     display(grad, cmap='gray')
    ret, thresh = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, rect_kernel)
    connected = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel=kernel)
#     display(connected, cmap='gray')
    ker = np.ones((11,11), dtype=np.uint8)
    diluted = cv2.dilate(connected, kernel=ker)
#     display(diluted, cmap='gray')
    
    contours, hierarchy = cv2.findContours(diluted.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    mask = np.zeros(thresh.shape, dtype=np.uint8)
#     display(mask, cmap='gray')
    print(os.path.join(text_dir, img_name[:-4]+'.txt'))
    # with open(os.path.join(text_dir, img[:-4]+'.txt'),'a+') as fp:
    fp = open(os.path.join(text_dir, img_name[:-4]+'.txt'),'a+')
    for idx in range(len(contours)):
        x,y,w,h = cv2.boundingRect(contours[idx])
        mask[y:y+h, x:x+w] = 0
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
        
        if r >0.45 and w > 8 and h > 8:
            tex = pytesseract.image_to_string(img[y:y+h, x:x+w])
            fp.write(tex)
#             ro = img[y-4:y+h+4, x-4:x+w+4]
#             display(ro, cmap='gray')
            cv2.rectangle(rgb, (x,y), (x+w,y+h), (0,255,0), 2)
    fp.close()
    contour_dir = os.path.join(os.getcwd(),'contours')
    cv2.imwrite(os.path.join(contour_dir,img_name[:-4]+'contours.jpg'),rgb) 
#     return contours

