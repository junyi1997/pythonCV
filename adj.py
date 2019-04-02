'''
將圖像轉會為可放入GUI的大小
'''


import cv2
import numpy as np
 
img = cv2.imread('test.jpg')
resImg1 = cv2.resize(img, (100,100), interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('resImg', resImg1)
cv2.waitKey()
 
cv2.destroyAllWindows()
