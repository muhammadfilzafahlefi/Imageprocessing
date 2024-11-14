import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()  # Unpack the return value
    if not ret:  # Check if frame is read correctly
        print("Failed to grab frame")
        break
    
    cv2.imshow("video", frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
