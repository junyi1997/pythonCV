
import cv2
import numpy as np
 
img = cv2.imread('test.jpg')
resImg1 = cv2.resize(img, (300,300), interpolation=cv2.INTER_CUBIC)

resImg2 = cv2.resize(img,(img.shape[1],img.shape[0]), interpolation=cv2.INTER_CUBIC)
img1 = cv2.resize(img, None, fx=0.1,fy=0.5,interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('resImg', resImg1)
cv2.imshow('resImg2', resImg2)
cv2.imshow('img1', img1)
cv2.waitKey()
 
cv2.destroyAllWindows()
