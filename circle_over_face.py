import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("baby.jpg")



output = img.copy()

circle_img = cv2.circle(img,(450,330), 200, (0,0,255), 2)
cv2.imshow ("circle", circle_img )

cv2.waitKey(0)
