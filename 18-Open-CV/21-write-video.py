import cv2

video = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('Output.mp4', fourcc, 30, (640,480))

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Resize to match VideoWriter resolution (optional but safer)
    frame = cv2.resize(frame, (640,480))

    output.write(frame)
    cv2.imshow('Frame', frame)

    # Press 's' to stop
    if cv2.waitKey(10) & 0xFF == ord('s'):
        break

# Release everything
video.release()
output.release()
cv2.destroyAllWindows()