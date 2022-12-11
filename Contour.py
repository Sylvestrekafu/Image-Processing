"""
Contour analysis is a technique used in image processing to detect objects in an image based on their shapes.
It involves identifying the outlines or "contours" of objects in an image and then using this information to extract
the objects and their bounding boxes (i.e., the rectangular regions that enclose each object).

Here is an example of how contour analysis can be used to retrieve bounding boxes in Python using the OpenCV library:
In this script, the image is first converted to grayscale and then thresholded
to create a binary image (i.e., an image with only black and white pixels).
This is because contour analysis works best on binary images.

Next, the cv2.findContours() function is used to find the contours (i.e., the outlines) of the objects in the binary image.
This function returns a list of contours, along with other information about the contours.

The script then loops through the list of contours and uses the cv2.boundingRect() function to compute
the bounding box (i.e., the rectangular region) of each contour.
This function returns the coordinates of the bounding box, along with its width and height.

Finally, the script draws the bounding boxes on the original image and saves the resulting image to a file.
"""
import cv2

# Read the image
img = cv2.imread("image.jpg")

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary image
_, img_threshold = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Find the contours in the image
_, contours, _ = cv2.findContours(img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through the contours and draw a bounding box around each one
for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

# Save the image with the bounding boxes
cv2.imwrite("bounding_boxes.jpg", img)
