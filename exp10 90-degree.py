import cv2

image = cv2.imread('D:/2023-07-02 tab images/tab images 1450.jpg')
rotated_image = cv2.rotate(image, cv2.ROTATE_180)
cv2.imwrite('rotated_image_180.jpg', rotated_image)
