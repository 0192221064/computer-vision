 
import cv2
cap = cv2.VideoCapture('D:/2023-07-02 tab images/tab images 1234.mp4')
if not cap.isOpened():
    print("Error: Unable to open video.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
