import cv2 as cv
import mediapipe as mp
import time

capture = cv.VideoCapture(1)

# init mediapipe module for hand detection
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

prev = 0
current = 0

while True:
    success, img = capture.read()

    rgbImg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    handResults = hands.process(rgbImg)
    if handResults.multi_hand_landmarks:
        for hand in handResults.multi_hand_landmarks:
            for id,landmark in enumerate(hand.landmark):
                height, width, channel = img.shape
                x,y = int(landmark.x * width), int(landmark.y * height)

            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)

    current= time.time()
    fps = int(1/(current-prev))
    prev = current

    cv.putText(img, str(fps), (10,70), cv.FONT_HERSHEY_SIMPLEX, 3, (255,0,255))

    cv.imshow("Image",img)
    if cv.waitKey(20) & 0xFF == 27:
        break
    
cv.destroyAllWindows()