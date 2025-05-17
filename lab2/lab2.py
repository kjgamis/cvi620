import cv2
import matplotlib.pyplot as plt
from numpy import sin, cos

# 1. read an image, convert to rgb and show the image

# image_orig = cv2.imread("dapper.jpg")
#
# image1 = cv2.cvtColor(image_orig, cv2.COLOR_BGR2RGB)
# image2 = cv2.cvtColor(image_orig, cv2.COLOR_BGR2HSV)
#
# cv2.imshow("Image RGB", image1)
# cv2.imshow("Image HSV", image2)
#
# cv2.waitKey()  # Wait indefinitely until a key is pressed
#
# cv2.destroyAllWindows()  # Close all OpenCV windows


# 2. Change the format of an image from PNG to JPG in your system using OpenCV.

# image_png = cv2.imwrite("image.png", image_orig)
# image_jpg = cv2.imread("image.png")
#
# cv2.imshow("Image JPG", image_jpg)
# cv2.waitKey()
#
# cv2.destroyAllWindows()  # Close all OpenCV windows

# 3. Read an image.
# - Display the image using OpenCV and Matplotlib.
# cv2.imshow("Image", image_orig)
# plt.imshow(image_orig)
# plt.show()


# - What differences do you observe?
# - Save the image using both OpenCV and Matplotlib.


# 4.
# - Add padding to all four sides of the image using a border of 50 pixels.
# Try at least three border types. What visual differences do you see?
# - How can you change the color of padding

import cv2
import matplotlib.pyplot as plt

# Read the image
image_orig = cv2.imread("dapper.jpg")
image_rgb = cv2.cvtColor(image_orig, cv2.COLOR_BGR2RGB)

# padding with different border types
border_constant = cv2.copyMakeBorder(image_rgb, 250, 250, 250, 250, cv2.BORDER_CONSTANT, value=[255, 0, 0])  # Red
# padding
border_reflect = cv2.copyMakeBorder(image_rgb, 250, 250, 250, 250, cv2.BORDER_REFLECT)
border_wrap = cv2.copyMakeBorder(image_rgb, 250, 250, 250, 250, cv2.BORDER_WRAP)

plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 4, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

# Constant border
plt.subplot(1, 4, 2)
plt.imshow(border_constant)
plt.title("Constant Border")
plt.axis("off")

# Reflect border
plt.subplot(1, 4, 3)
plt.imshow(border_reflect)
plt.title("Reflect Border")
plt.axis("off")

# Wrap border
plt.subplot(1, 4, 4)
plt.imshow(border_wrap)
plt.title("Wrap Border")
plt.axis("off")

plt.tight_layout()
plt.show()

# padding colour can be changed by changing the `value` arg in `cv2.copyMakeBorder`


# 5. You are building a simple image processing pipeline. Your goal is to:
#
# - Keep the original image unchanged.
# - Create a version with a red square in the top-left corner.
#
# What would you do?


# 6. Plot the function y = x^2+6 using Matplotlib.

# 7. Plot sin(x) and cos(x) on the same figure. Add grid, labels, title, and legend.

# 8. Read an image and display it alongside its grayscaled version using matplotlib.


# 9. Having an image, create a 1x3 subplot that shows:
#
# - Original RGB image
# - Red channel
# - HSV version
# - Adjust the figure size for better visualization.

# image_orig = cv2.imread("dapper.jpg")
# image_rgb = cv2.cvtColor(image_orig, cv2.COLOR_BGR2RGB)
# image_hsv = cv2.cvtColor(image_orig, cv2.COLOR_BGR2HSV)
#
# # Original RGB image
# plt.subplot(131)
# plt.imshow(image_rgb)
# plt.title("Original RGB")
#
# # Red channel
# plt.subplot(132)
# plt.imshow(image_rgb[:, :, 0], cmap="Reds")
# plt.title("Red Channel")
#
# # HSV version
# plt.subplot(133)
# plt.imshow(image_hsv)
# plt.title("HSV Version")
#
# plt.show()

# 10. Search about Histograms and explain them. Plot a sample histogram below.
