import cv2
import numpy as np
import random


face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade=cv2.CascadeClassifier('smile.xml')

cap=cv2.VideoCapture(0)

run=True
while run:
    ret, img =cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=img[y:y+h, x:x+w]
        smiles=smile_cascade.detectMultiScale(roi_gray, 1.05, 5)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw,sy+sh), (255,255,0), 2)
        if cv2.waitKey(1) & 0xff==ord('s'):
            cv2.imwrite(f"{str(random.randint(10000))}.png", img)
            break

    cv2.imshow('img_smile', img)


    if cv2.waitKey(2) & 0xff==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
