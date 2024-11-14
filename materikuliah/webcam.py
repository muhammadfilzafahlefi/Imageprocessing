import cv2
cam = cv2.VideoCapture(0)
while True:
    frame = cam.read()
    cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break