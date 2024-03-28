import cv2
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
input_image = cv2.imread('D:/2023-07-02 tab images/tab images 1623.jpg')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
smiles = smile_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in smiles:
    cv2.rectangle(input_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Smile Detection', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
