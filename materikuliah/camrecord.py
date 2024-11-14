import cv2
import os

# Create a folder to store recordings if it doesn't exist
output_folder = "recordings"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cam = cv2.VideoCapture(0)
recording = False  # Toggle for recording
out = None  # Video writer object

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("video", frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    elif key == ord('f'):  # Take snapshot
        filename = f"{output_folder}/snapshot.png"
        cv2.imwrite(filename, frame)
        print(f"Snapshot saved as {filename}")
    elif key == ord('r'):  # Toggle recording
        recording = not recording
        if recording:
            # Define the codec and create VideoWriter object
            filename = f"{output_folder}/recording.mp4"
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(filename, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            print(f"Recording started, saving to {filename}")
        else:
            # Stop recording
            out.release()
            out = None
            print("Recording stopped")

    # Write the frame to the file if recording is on
    if recording and out is not None:
        out.write(frame)

cam.release()
if out:
    out.release()
cv2.destroyAllWindows()
