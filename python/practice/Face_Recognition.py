import cv2

# Use the default camera (0) or replace with a valid video file path
capture = cv2.VideoCapture(0)

# Check if the video source is opened successfully
if not capture.isOpened():
    print("Error: Could not open video source.")
    exit()

# Set width and height for the video capture
capture.set(3, 640)  # Width
capture.set(4, 740)  # Height

while True:
    # Read frames from the video source
    success, img = capture.read()
    if not success:
        print("Error: Failed to capture frame.")
        break  # Exit if frame capture fails

    # Display the frame
    cv2.imshow("FACE", img)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
capture.release()
cv2.destroyAllWindows()
