import imp
import cv2.cv2 as cv
import os

path=os.getcwd()
tif_list=[x for x in os.listdir(path) if x.endswith(".tif")]
for num,i in enumerate(tif_list):
    img=cv.imread(i,-1)
    cv.imwrite(i.split('.')[0]+".jpg",img)