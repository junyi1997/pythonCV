'''
將圖像轉會為可放入GUI的大小
'''


import cv2
import numpy as np
import com
img = cv2.imread(com.file_name)
resImg1 = cv2.resize(img, (100,100), interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('resImg', resImg1)
cv2.waitKey()
 
cv2.destroyAllWindows()
