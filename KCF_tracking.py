"""
Object tracking is the process of identifying and following an object in a video sequence.
In Python, there are several libraries and techniques you can use to perform object tracking.

One popular library for object tracking in Python is OpenCV.
This library provides functions for image processing and computer vision, including functions for object tracking.
For example, you can use the OpenCV library to apply the KCF (Kernelized Correlation Filters)
algorithm to a video to track objects in the video. Here is an example:

In this example, the OpenCV library is used to apply the KCF algorithm to a video to track objects in the video.
The cv2.TrackerKCF_create() function is used to create a KCF tracker object, and the cv2.VideoCapture() function is used to open the video file.
The cv2.selectROI() function is used to select the object to be tracked in the first frame of the video,
and the init() method is used to initialize the tracker with the bounding box coordinates of the selected object.
The update() method is then used to update the tracker in each frame of the video,
and a rectangle is drawn around the tracked object if the tracking was successful. The frames of the video are displayed using the `cv
"""

import cv2

# Create a KCF tracker object
tracker = cv2.TrackerKCF_create()

# Open the video file
video = cv2.VideoCapture('my-video.mp4')

# Read the first frame of the video
success, frame = video.read()

# Check if the video was successfully opened
if not success:
    print('Error: Could not open video file.')
    exit(1)

# Select the object to be tracked in the first frame
bbox = cv2.selectROI('Tracking', frame, fromCenter=False, showCrosshair=True)

# Initialize the tracker with the bounding box coordinates
tracker.init(frame, bbox)

# Loop over the frames of the video
while True:
    # Read the next frame
    success, frame = video.read()

    # Check if the video has ended
    if not success:
        break

    # Update the tracker
    success, bbox = tracker.update(frame)

    # Check if the tracking was successful
    if success:
        # Draw a rectangle around the tracked object
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
    else:
        # Tracking failed
        cv2.putText(frame, 'Tracking failed', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Tracking', frame)

    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
video.release()
cv2.destroyAllWindows()
