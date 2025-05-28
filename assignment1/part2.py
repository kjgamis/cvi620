# Instructions:
# Write a Python script to manually blend two images using NumPy operations.
# Use the following formula to blend them:
# blend = (1−α)⋅img1 + α⋅img2
# • alpha must be a value between 0 and 1.
# • Do not use cv2.addWeighted.
# • Display and save the blended image as "manual_blend.jpg"

import cv2
import numpy as np

# Load two images

img1 = cv2.imread('dapper-ship.jpeg')
img2 = cv2.imread('dapper-look.jpeg')

# Check if images were loaded successfully
if img1 is None or img2 is None:
    raise ValueError("One or both images could not be loaded. Check the file paths.")

# Set alpha value for blending
alpha = 0.5  # Adjust this value between 0 and 1 for different blending effects

# Blend the images using the formula
blend = (1 - alpha) * img1 + alpha * img2

# Convert the blended image to uint8 type
blend = np.clip(blend, 0, 255).astype(np.uint8)

# Display the blended image
cv2.imshow("Manual Blend", blend)

# Save the blended image
cv2.imwrite("manual_blend.jpg", blend)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()

