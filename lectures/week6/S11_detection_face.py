import cv2

image = cv2.imread('S11_Lenna.png')
# image = cv2.imread('S11_collage_faces.jpg')

# convert to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml') 
eyes_detector = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')

faces = face_detector.detectMultiScale(image_gray, scaleFactor=1.2, minNeighbors=2) # scaleFactor is the scale of the image, minNeighbors is the number of neighbors for each face

for (x, y, w, h) in faces:
  # draw a blue rectangle around the face
  # (255, 0, 0) is the color of the rectangle
  # 2 is the thickness of the rectangle
  # (x, y) is the top left corner of the rectangle
  # (x + w, y + h) is the bottom right corner of the rectangle
  cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
  roi = image_gray[y:y+h, x:x+w] # region of interest (face)

  eyes = eyes_detector.detectMultiScale(roi, scaleFactor=1.2, minNeighbors=2)
  print(eyes)

  # draw a red rectangle around the eyes of the original image
  for (x2, y2, w2, h2) in eyes:
    cv2.rectangle(image, (x2+x, y2+y), (x2+x+w2, y2+y+h2), (0, 0, 255), 2)

cv2.imshow('frame', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
