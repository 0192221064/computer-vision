import cv2
import numpy as np

img = cv2.imread('C:/Users/Lenovo/Pictures/2023-07-02 images/WhatsApp Image 2024-03-23 at 12.55.17 PM.jpeg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (100, 50, 50), (140, 255, 255))
result = cv2.bitwise_and(img, img, mask=~mask)

cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
