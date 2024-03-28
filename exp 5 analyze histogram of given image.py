import cv2
image_path = input("Enter path to the input image: ")
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found or unable to read the image.")
    exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray_image], [0], None, [256], [0,256])
hist /= hist.max()
canvas = (255 * hist).astype(np.uint8)
cv2.imshow('Grayscale Histogram', cv2.resize(canvas, (256, 100)))
cv2.waitKey(0)
cv2.destroyAllWindows()
