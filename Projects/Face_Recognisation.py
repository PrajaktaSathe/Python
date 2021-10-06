import cv2
import numpy as np

face_Reg = cv2.CascadeClassifier('haarcascade_frontalface_default')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
     ret, vid = cap.read()
     faces = face_Reg.detectMultiScale(
        vid,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
     for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x+w, y+h), (0, 255, 0), 2)
     cv2.imshow('frame', vid)
     k = cv2.waitKey(30) & 0xff
     if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
