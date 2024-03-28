import cv2
image = cv2.imread('E:/cv files/cv images/images (1).jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
