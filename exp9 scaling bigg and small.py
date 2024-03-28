
import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("E:/cv files/cv images/images (1).jpeg",cv2.IMREAD_COLOR)
img = cv2.resize(img,(600,600))
cv2.imshow("Output image",img)
cv2.waitKey(0)
