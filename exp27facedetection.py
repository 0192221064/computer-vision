import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
input_image = cv2.imread('D:/2023-07-02 tab images/tab images 1450.jpg')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(input_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Face Detection', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
