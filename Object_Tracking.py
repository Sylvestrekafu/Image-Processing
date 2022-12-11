"""
Object tracking is the process of identifying and locating a moving object in a video sequence.
This can be useful for a variety of applications, such as surveillance, robotics, and driver assistance.

In Python, you can perform object tracking using the cv2 (OpenCV) module. Here is an example of how you might do this:

In this example, we use the TrackerKCF_create function to create an object tracker, which we then use to track the object in the video.
The bounding box for the object is selected manually using the selectROI function, and the tracker is initialized with this bounding box.
The update method is then called on each frame of the video, which returns the updated bounding box for the object.
The bounding box can then be drawn on the frame to show the object's location.
"""
import cv2

# Read the video file or  Open the video file
cap = cv2.VideoCapture('video.mp4')

# Create an object tracker
tracker = cv2.TrackerKCF_create()

# Read the first frame from the video
_, frame = cap.read()

# Select the bounding box for the object to be tracked
bbox = cv2.selectROI(frame, False)

# Initialize the tracker with the selected bounding box
tracker.init(frame, bbox)

while True:
    # Read a frame from the video
    _, frame = cap.read()

    # Update the tracker
    success, bbox = tracker.update(frame)

    # If the tracker is successful
    if success:
        # Draw the bounding box
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

    # Display the frame
    cv2.imshow('Tracking', frame)

    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy any open windows
cap.release()
cv2.destroyAllWindows()
