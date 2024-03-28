import cv2
image_path = input("C:/Users/Lenovo/Pictures/2023-07-02 tab images/tab images 1418")
image = cv2.imread(image_path)
text = input("Enter text: ")
cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow("Image with Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
