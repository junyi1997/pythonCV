
import cv2
import numpy as np
 
img = cv2.imread('test.jpg')
resImg1 = cv2.resize(img, (300,300), interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('resImg', resImg1)
cv2.waitKey()
 
cv2.destroyAllWindows()
