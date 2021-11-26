import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=np.float32(gray)
    dst=cv2.cornerHarris(gray,2,3,0.04)
    dst=cv2.dilate(dst,None)
    frame[dst>0.01*dst.max()]=[255,0,255]
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==27:  #27 means ESC key
        break
cap.release()
cv2.destroyAllWindows()