import cv2
vehicle_cascade = cv2.CascadeClassifier('D:/opencv/data/haarcascades/haarcascade_car.xml')
input_image = cv2.imread('D:/2023-07-02 tab images/tab images 5518.jpg')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
vehicles = vehicle_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in vehicles:
    cv2.rectangle(input_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Vehicle Detection', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
