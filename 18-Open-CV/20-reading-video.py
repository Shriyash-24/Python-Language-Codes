import cv2
video = cv2.VideoCapture("C:/Users/Shri/Coding/Additional-Files/vid.mp4")

while video.isOpened():
    ret, frame = video.read() # ret --> True if a frame is read, frame is actual image.
    if not ret: # if video ends, ret will be false
        break
    frame = cv2.resize(frame,(800,720))
    cv2.imshow("Output",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

