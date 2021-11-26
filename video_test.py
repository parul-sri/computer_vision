# pip install opencv-contrib-python
import cv2

cap=cv2.VideoCapture("new.mp4")
while True:
    ret, frame=cap.read()
    if ret:
        cv2.imshow('window',frame)
        if cv2.waitKey(1)& 0xFF==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()