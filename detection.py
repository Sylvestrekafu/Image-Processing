"""
In this code, we first load the cascade file for detecting faces, which contains the trained machine learning model for detecting faces. This file is typically pre-trained and provided by OpenCV. Then, we load the input image and convert it to grayscale, as the cascade file expects grayscale images.

Next, we use the detectMultiScale method of the face_cascade object to look for faces in the image. This method returns a list of bounding boxes for the faces it detected in the image.

Finally, we loop through the list of bounding boxes and draw a rectangle around each face using the rectangle method of the cv2 object. We then save the image with the detected faces to a file.

Of course, this is just a simple example and you can customize it to your specific needs. For example, you can change the cascade file to detect other objects, such as eyes or cars. You can also adjust the parameters of the detectMultiScale method to improve the accuracy of the object detection.


"""
import cv2

# Load the cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Save the result image
cv2.imwrite('result.jpg', img)
