"""
To use the CSRT tracker in Python, you will first need to install the OpenCV library.
 You can do this using the pip package manager with the following command:

 pip install opencv-python

 Once you have installed OpenCV, you can use the following code to create a CSRT tracker object and track an object in a video sequence:

In this code, the cv2.TrackerCSRT_create() function creates a CSRT tracker object, and the tracker.init()
method initializes the tracker with the first frame of the video and the bounding box of the object you want to track.
The tracker.update() method is then called in each subsequent frame to update the tracker with the current frame.
 The bounding box is drawn on the frame, and the resulting frame is displayed to the user.
"""

import cv2

# create a CSRT tracker object
tracker = cv2.TrackerCSRT_create()

# initialize the tracker with the first frame of the video and the bounding box
# of the object you want to track
success = tracker.init(frame, bounding_box)

while True:
  # read the next frame of the video
  success, frame = video.read()

  # update the tracker with the current frame
  success, bbox = tracker.update(frame)

  # draw the bounding box on the frame
  if success:
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)

  # show the frame
  cv2.imshow("Tracking", frame)

  # exit if the user presses the 'q' key
  if cv2.waitKey(1) & 0xff == ord('q'):
    break
