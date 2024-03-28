import cv2

input_video = cv2.VideoCapture('D:/2023-07-02 tab images/tab images 1234.mp4')
fps, frame_count, width, height = [input_video.get(prop) for prop in [cv2.CAP_PROP_FPS, cv2.CAP_PROP_FRAME_COUNT, cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT]]
output_video = cv2.VideoWriter('reversed_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (int(width), int(height)))
[output_video.write(input_video.read()[1]) for _ in range(int(frame_count))]
input_video.release()
output_video.release()
cv2.destroyAllWindows()
