"""
To plot a histogram of an RGB image using OpenCV in Python, you can use the calcHist method of the cv2 module to calculate
the histogram values for each channel, and then use the plot method of the matplotlib library to plot the histograms.
Here is an example of how you could do this:

In this code, we first load the image and then use the calcHist method
to calculate the histogram values for each channel (blue, green, and red). Then, we use the plot method of the matplotlib library to plot the histogram values for each channel.

Finally, we add a legend to the plot to show which color corresponds to which channel, and we use the show method to display the plot.
"""
import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('image.jpg')

# Calculate the histogram values for each channel
hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])

# Plot the histogram for each channel
plt.plot(hist_b)
plt.plot(hist_g)
plt.plot(hist_r)

# Add a legend
plt.legend(['Blue', 'Green', 'Red'])

# Show the plot
plt.show()
