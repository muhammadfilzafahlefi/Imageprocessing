import cv2
import time

# Load the Haar Cascade for car detection
car_cascade = cv2.CascadeClassifier('haarcascade/cars.xml')

# Open the video file
cap = cv2.VideoCapture('recordings/video1.avi')

# Initialize variables
fps = cap.get(cv2.CAP_PROP_FPS)  # Get frames per second of the video
frame_time = 1 / fps  # Time per frame
scale_factor = 0.05  # Scale factor for converting pixels to real-world distance
previous_centers = {}  # Store previous centers of detected cars by ID

# Speed adjustment factor
speed_factor = 1.0  # Starts at normal speed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    current_centers = {}  # Temporary storage for current centers

    # Calculate speed for each detected car
    for (x, y, w, h) in cars:
        center_x = x + w // 2
        center_y = y + h // 2
        current_center = (center_x, center_y)
        car_id = (x, y, w, h)  # Simple ID based on detection box position

        # Draw rectangle around the car
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle

        # Check if the car ID exists in previous_centers
        if car_id in previous_centers:
            # Calculate distance in pixels
            distance = ((current_center[0] - previous_centers[car_id][0]) ** 2 +
                         (current_center[1] - previous_centers[car_id][1]) ** 2) ** 0.5

            # Convert to real-world distance (in meters)
            real_world_distance = distance * scale_factor
            
            # Calculate speed in m/s
            speed = real_world_distance / frame_time  # m/s
            speed_kmh = speed * 3.6  # Convert to km/h

            # Display the speed on the frame
            cv2.putText(frame, f'Speed: {speed_kmh:.2f} km/h', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Update previous center for the car
        previous_centers[car_id] = current_center

    # Display the frame
    cv2.imshow('Car Speed Detection', frame)

    # Calculate the adjusted wait time for the playback speed
    wait_time = int((1000 / fps) / speed_factor)  # Adjust wait time based on speed factor
    
    # Handle user input for speed adjustment
    key = cv2.waitKey(wait_time) & 0xFF
    if key == ord('q'):  # Quit
        break
    elif key == ord('+'):  # Speed up
        speed_factor = min(4.0, speed_factor * 1.2)  # Cap the speed to 4x
    elif key == ord('-'):  # Slow down
        speed_factor = max(0.25, speed_factor / 1.2)  # Minimum speed is 0.25x

cap.release()
cv2.destroyAllWindows()
