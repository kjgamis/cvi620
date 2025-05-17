import cv2
import numpy as np

image = cv2.imread("dapper.jpg")

# print(f"iamge array is: {image}")

# cv2.imshow("Original", image)
cv2.imshow("Red", image[:, :, 0])  # Display the blue channel
cv2.imshow("Green", image[:, :, 1])  # Display the green channel
cv2.imshow("Blue", image[:, :, 2])  # Display the red channel
cv2.waitKey(0)  # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()  # Close all OpenCV windows


# rows, cols, channels = image.shape
# print(f"rows: {rows}, cols: {cols}, channels: {channels}")


a = [1, 2, 3]
b = a

print(f"a: {a}")
print(f"b: {b}")

b[0] = 10

print(f"a: {a}")
print(f"b: {b}")

