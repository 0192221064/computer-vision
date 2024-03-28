import numpy as np
import cv2
size = int(input("Enter the size of the image: "))
image = np.ones((size, size, 3), dtype=np.uint8) * 255
box_size = size // 10
image[:box_size, :box_size] = [0, 0, 0]
image[:box_size, -box_size:] = [255, 0, 0]
image[-box_size:, :box_size] = [0, 255, 0]
image[-box_size:, -box_size:] = [0, 0, 255]
cv2.imshow("Image with Colored Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
