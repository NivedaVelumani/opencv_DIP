import cv2
import numpy 
import imutils


img=cv2.imread("car.jpg")
img_translate=imutils.translate(img, -650, 50)
img_show=cv2.imshow("TRANSLATED_IMAGE", img_translate)
img=cv2.imshow("Originalimage", img)
cv2.waitKey(0)
