import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8) # uint8 is a data type for images

# make the background white
image[:] = (255, 255, 255)  # Set the entire image to white
# Draw black triangle for cutout
middle_triangle = np.array([[250, 120], [187, 250], [330, 250]], np.int32)
inverted_triangle = np.array([[290, 180], [370, 180], [330, 250]], np.int32)

# shape positions
top_circle = (250, 120)
bottom_left_circle = (175, 250)
bottom_right_circle = (325, 250)

# colors in BGR format
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

circle_radius = 50
circle_thickness = 40

# red circle at the top
cv2.circle(image, top_circle, circle_radius, red, circle_thickness)
# green circle at the bottom left
cv2.circle(image, bottom_left_circle, circle_radius, green, circle_thickness)
# Center triangle
cv2.fillPoly(image, [middle_triangle], white)
# blue circle at the bottom right
cv2.circle(image, bottom_right_circle, circle_radius, blue, circle_thickness)
# inverted triangle cutout
cv2.fillPoly(image, [inverted_triangle], white)

# Draw the OpenCV logo text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "OpenCV", (130, 400), font, 2, black, 6, cv2.LINE_AA)

# Display the image
cv2.imshow("OpenCV logo", image)  # Show the image in a window
cv2.waitKey(0)
cv2.destroyAllWindows()
