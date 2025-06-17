import cv2

cap = cv2.VideoCapture('S11_video_cars.mp4')
plate_detector = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')

while True:
  ret, frame = cap.read() # read the frame from the video
  frame = cv2.resize(frame, (1000, 600))
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  plates = plate_detector.detectMultiScale(frame, 1.5, 5)

  for (x, y, w, h) in plates:
    cv2.rectangle(frame, (x, y), (x+w, y+ h), (0, 0, 255), 4)

  cv2.imshow('frame', frame)
  cv2.waitKey(1)

cv2.destroyAllWindows()
