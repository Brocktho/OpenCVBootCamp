import cv2 as cv
import mediapipe as mp
import time

class HandDetector():
    def __init__(self,
                static_image_mode=False,
                max_num_hands=2,
                model_complexity=1,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5):
        self.mode = static_image_mode
        self.maxHands = max_num_hands
        self.complexity = model_complexity
        self.detectionConfidence = min_detection_confidence
        self.trackingConfidence = min_tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complexity, self.detectionConfidence, self.trackingConfidence)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHands(self, img, draw=True):
        handResults = self.hands.process(img)
        if handResults.multi_hand_landmarks:
            for hand in handResults.multi_hand_landmarks:
                for id,landmark in enumerate(hand.landmarks):
                    height, width, channel = img.shape
                    x,y = int(landmark.x * width), int(landmark.y * height)
                    return (id,x,y)
        



def main():
    capture = cv.VideoCapture(1)

    # init mediapipe module for hand detection
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    prev = 0
    current = 0
    while True:
        success, img = capture.read()

        rgbimg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        handResults = hands.process(rgbimg)
        if handResults.multi_hand_landmarks:
            for hand in handResults.multi_hand_landmarks:
                for id,landmark in enumerate(hand.landmarks):
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


if __name__ == "__main__":
    main()