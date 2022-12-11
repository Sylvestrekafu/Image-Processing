"""
Contour detection is a technique for finding the boundaries of objects in an image. In the context of computer vision,
contours are curves that connect adjacent points with the same intensity value. Using contour detection,
 it is possible to find shapes and objects in an image, and then analyze and manipulate them.
 OpenCV is a popular library for computer vision tasks, and it includes functions for performing contour detection.
To use contour detection in OpenCV, you can follow these steps:

1-Load the input image into a NumPy array.
2-Convert the image to grayscale, to simplify the contour detection process.
3-Use the cv2.Canny() function to detect edges in the image.
This function uses the Canny edge detection algorithm to find the boundaries of objects in the image.
4-Use the cv2.findContours() function to detect contours in the image. This function takes the input image and the edge map as input
 and returns a list of contours and hierarchy information.
5- Use the cv2.drawContours() function to draw the contours on the original image. This function takes the input image, the contours, and an index of the contour to draw as input,
  and returns the image with the contours drawn on it.

This code will load the input image, convert it to grayscale, detect edges using the Canny edge detection algorithm,
find contours in the image, and then draw the contours on the original image.
The resulting image will show the contours of the objects in the input image.
Here is an example of using contour detection in OpenCV to detect the shapes in an image:

"""
import cv2
import numpy as np

# Load the input image
image = cv2.imread('input.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges in the image
edges = cv2.Canny(gray, 100, 200)

# Find contours in the image
_, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
contour_image = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Show the image with the contours
cv2.imshow('Contours', contour_image)
cv2.waitKey(0)
