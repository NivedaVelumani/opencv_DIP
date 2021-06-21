import cv2
import numpy
import imutils

#img read 
img=cv2.imread("ball.jpg")

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

#image show
imgshow=cv2.imshow("Image", img)
cv2.waitKey()
