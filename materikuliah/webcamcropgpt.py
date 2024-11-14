import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    height, width, _ = frame.shape
    print(height, '-', width)

    # Split the frame into left and right halves
    frameleft = frame[0:height, 0:int(width/2)]
    frameright = frame[0:height, int(width/2):width]

    cv2.imshow('video', frame)
    cv2.imshow('video Left', frameleft)
    cv2.imshow('video Right', frameright)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

