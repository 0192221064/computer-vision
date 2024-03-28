import cv2
import numpy as np

image = cv2.imread('D:/2023-07-02 tab images/tab images 1450.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corners = cv2.cornerHarris(gray, 2, 3, 0.04)
corners = cv2.dilate(corners, None)
threshold = 0.01 * corners.max()
corner_points = np.where(corners > threshold)
for y, x in zip(*corner_points):
    cv2.circle(image, (x, y), 5, (0, 255, 0), 2)
cv2.imshow('Corners Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
