import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 for default webcam

# Loop to continuously get frames
while True:
    success, frame = cap.read()  # Read the frame
    if not success:
        print("❌ Failed to grab frame")
        break

    cv2.imshow("Live Feed", frame)  # Show frame in a window

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()

