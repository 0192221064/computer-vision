import cv2
import numpy as np
image = cv2.imread('E:/cv files/cv images/images (1).jpeg')
lower_bound = np.array([100, 0, 0], dtype=np.uint8)
upper_bound = np.array([255, 50, 50], dtype=np.uint8)
mask = cv2.inRange(cv2.cvtColor(image, cv2.COLOR_RGB2BGR), lower_bound, upper_bound)
foreground_subtracted_image = cv2.cvtColor(cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask)), cv2.COLOR_BGR2RGB)
cv2.imshow('Foreground Subtracted Image', foreground_subtracted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
