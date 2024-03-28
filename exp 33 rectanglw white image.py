import numpy as np
import cv2
w, h = map(int, input("Width Height: ").split())
img = np.full((h, w, 3), 255, dtype=np.uint8)
cv2.rectangle(img, (w//4, h//4), (3*w//4, 3*h//4), (0, 0, 0), 2)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
