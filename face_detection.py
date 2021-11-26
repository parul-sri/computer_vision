import cv2
import mediapipe as mp

mp_face_detection=mp.solutions.face_detection
mp_draw=mp.solutions.drawing_utils

#webcam code
cap=cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(
    model_selection=0,min_detection_confidence=.5
) as face_detection:
    while cap.isOpened():
        success, img=cap.read()
        if not success:
            print("ignoring empty camera frame")
            continue
        img.flags.writeable=False
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=face_detection.process(img)

        #draw on the face
        img.flags.writeable=True
        img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

        if results.detections:
            for detection in results.detections:
                    mp_draw.draw_detection(img,detection)
        cv2.imshow("Face Detection",img)
        if cv2.waitKey(2)==27:
            break
    cap.release()
    cv2.destroyAllWindows()

            
