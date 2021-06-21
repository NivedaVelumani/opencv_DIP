import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("baby.jpg")




# draw green text on the image
output = img.copy()
cv2.putText(output, "BABY", (180, 250),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 250, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
