import cv2
image=cv2.imread('test.jpg') 
res=cv2.resize(image,(32,32),interpolation=cv2.INTER_CUBIC) 
cv2.imshow('iker',res) 
cv2.imshow('image', image) 
cv2.waitKey(0) 
cv2.destoryAllWindows()
