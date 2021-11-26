import cv2
import mediapipe as mp
import time
import pyautogui as gui

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
is_playing = False
gui.click(700,30)
while True:
    success, img = cap.read()
    img = cv2.flip(img,3)
    imgRGB = cv2.cvtColor(img,  cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape      
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                if id == 8:
                    print(cx,cy)
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    if not is_playing and cx > 175 and cx < 350 and cy > 0 and cy < 250:
                        gui.press('space')
                        is_playing = True
                    if is_playing and cx > 0 and cx < 175 and cy >0 and cy < 250:
                        gui.press('space')
                        is_playing = False
                    if   cx > 350 and cx < 500 and cy > 0 and cy < 250:
                        gui.press('volumeup')
                    if   cx > 350 and cx < 500 and cy > 250 and cy < 500:
                        gui.press('volumedown')
                        
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image",img)
    if cv2.waitKey(2)==27:
            break
cap.release()
cv2.destroyAllWindows()
