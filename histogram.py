"""
To plot a histogram using OpenCV in Python, you can use the calcHist method of the cv2 module to calculate the histogram values,
and then use the plot method of the matplotlib library to plot the histogram.
Here is an example of how you could do this:

n this code, we first load the image and convert it to grayscale, as the calcHist method expects grayscale images.
Then, we use the calcHist method to calculate the histogram values for the grayscale image.

Next, we use the plot method of the matplotlib library to plot the histogram values.
Finally, we use the show method to display the plot.

You can customize this code to your specific needs. For example, you can change the number of bins in the histogram,
or you can plot multiple histograms for different channels of a color image. You can also customize the plot appearance
using the various options available in the matplotlib library.
"""

import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the histogram values
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot the histogram using matplotlib
plt.plot(hist)
plt.show()
