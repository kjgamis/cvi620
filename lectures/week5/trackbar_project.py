import cv2
import numpy as np
import matplotlib.pyplot as plt

def empty(a):
    pass

img = cv2.imread('S9_Lambo.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow('TrackBars')
cv2.createTrackbar('H min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('H max', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('S min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('S max', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('V min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('V max', 'TrackBars', 0, 255, empty)

# cv2.imshow('frame', img)


while True:
    h_min = cv2.getTrackbarPos('H min', 'TrackBars')
    h_max = cv2.getTrackbarPos('H max', 'TrackBars')
    s_min = cv2.getTrackbarPos('S min', 'TrackBars')
    s_max = cv2.getTrackbarPos('S max', 'TrackBars')
    v_min = cv2.getTrackbarPos('V min', 'TrackBars')
    v_max = cv2.getTrackbarPos('V max', 'TrackBars')
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    roi = cv2.bitwise_and(img, img, mask=mask)
    
    cv2.imshow('original', img)
    cv2.imshow('hsv', img_hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('roi', roi)

    cv2.waitKey(100)

    
cv2.destroyAllWindows()
