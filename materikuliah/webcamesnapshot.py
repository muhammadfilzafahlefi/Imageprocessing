import cv2

cam = cv2.VideoCapture(0)
snapshot_count = 0  # Counter to save multiple snapshots

while True:
    ret, frame = cam.read()  # Unpack the return value
    if not ret:  # Check if frame is read correctly
        print("Failed to grab frame")
        break
    
    cv2.imshow("video", frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('f'):
        # Save the snapshot
        snapshot_filename = f"snapshot_{snapshot_count}.png"
        cv2.imwrite(snapshot_filename, frame)
        print(f"Snapshot saved as {snapshot_filename}")
        snapshot_count += 1  # Increment the counter for unique filenames

cam.release()
cv2.destroyAllWindows()
