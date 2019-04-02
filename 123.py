import cv2

im1 = cv2.imread('lena.jpg')
cv2.imshow('image1', im1)
cv2.waitKey(0)

im2 = cv2.resize(im1, (10,10), interpolation=cv2.INTER_CUBIC)
cv2.imshow('image2', im2)
cv2.waitKey(0)
cv2.imwrite('lena2.jpg', im2)
