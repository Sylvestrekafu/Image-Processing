import cv2
import matplotlib.pyplot as plt
# read the image
image=cv2.imread('image_name.jpg')
#convert to RGB
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# plot the image
plt.imshow(image)
# plot the histogram
plt.hist(image.ravel(),256,[0,256])
plt.title('RGB Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()