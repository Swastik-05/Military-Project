"""This is a sample code submitted for hackathon verification as requested by organizers. To prevent potential leaks, sensitive keys and methods are not shared
as i was told by the lead organiser that project leak can not be guaranteed."""
import cv2

# Start the webcam
cam = cv2.VideoCapture(1)
if not cam.isOpened():
    print("Cannot open webcam")
    exit()

# Load face detection model
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("Starting face detection demo")

while True:
    # Read a frame from the webcam
    ret, img = cam.read()
    if not ret:
        print("Cannot read webcam frame")
        break

    # Convert to grayscale for detection
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(gray_img, 1.3, 5)

    # Draw rectangles and labels on faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Simulate recognition with dummy label
        label = "Known" if w > 100 else "Unknown"  # Simple rule for demo
        cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the video feed
    cv2.imshow('Face Detection Demo - Press Q to Exit', img)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cam.release()
cv2.destroyAllWindows()
