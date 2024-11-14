import cv2
import os

# Create a folder for snapshots if it doesn't exist
snapshot_folder = 'snapshots'
if not os.path.exists(snapshot_folder):
    os.makedirs(snapshot_folder)

# Load the Haar Cascade
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt.xml')

# Open video capture
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale (Haar Cascades work better on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw yellow rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Yellow color

        # Check for 'r' key press to take a snapshot of the detected face area
        if cv2.waitKey(1) & 0xFF == ord('r'):
            # Crop the face area from the frame
            face_area = frame[y:y + h, x:x + w]
            # Save the snapshot with a unique filename in the specified folder
            snapshot_filename = os.path.join(snapshot_folder, 'snapshot_face.png')  # Change this to a dynamic filename if needed
            cv2.imwrite(snapshot_filename, face_area)
            print(f"Snapshot saved as {snapshot_filename}")

    # Display the output
    cv2.imshow("Face Detection", frame)

    # Break on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
