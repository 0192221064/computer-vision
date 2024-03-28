import numpy as np
import cv2
size = int(input("Enter the size of the image: "))
white_image = np.ones((size, size, 3), dtype=np.uint8) * 255
center = (size // 2, size // 2)
radius = min(size // 4, size // 2)
cv2.circle(white_image, center, radius, (0, 0, 0), -1)
cv2.imshow('White Image with Circle', white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
