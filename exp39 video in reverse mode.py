import cv2

video_path = 'D:/2023-07-02 tab images/tab images 1234.mp4'
slow_factor = 2 

cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('output_reverse_slow.avi', cv2.VideoWriter_fourcc(*'XVID'), fps / slow_factor, (int(cap.get(3)), int(cap.get(4))))

for frame_number in range(total_frames - 1, -1, -1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    if ret:
        out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
