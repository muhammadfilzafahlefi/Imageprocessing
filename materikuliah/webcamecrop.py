import cv2
 cam = cv2.VideoCapture(0)
while True:
 _,frame = cam.read()
 height, width, _ = frame.shape
 print (height, '-',width)
 frameleft = frame[0:height, 0:int(width/2)]
 frameright = frame[0:height, 0:int(width/2):width]

 cv2.imshow('video', frame)
 cv2.imshow('video Left', frameleft)
 cv2.imshow('video Right', frameright)

 
  key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
