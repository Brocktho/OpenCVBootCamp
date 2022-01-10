import numpy as np
import cv2 as cv

def nothing(x):
    pass



img = np.zeros((500,500,3), np.uint8)
cv.namedWindow("canvas")

cv.createTrackbar("R", "canvas", 0, 255, nothing)
cv.createTrackbar("B", "canvas", 0, 255, nothing)
cv.createTrackbar("G", "canvas", 0, 255, nothing)
cv.createTrackbar("Pen", "canvas", 0, 64, nothing)
drawing = False
erasing = False
r = 0
g = 0
b = 0 
size = 1
def draw(event, x, y, flags, params):
    global r, g, b, size, drawing, erasing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        cv.circle(img, (x,y), size, (b,g,r), -1)
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img, (x,y), size, (b,g,r), -1)
        elif erasing:
            cv.circle(img, (x,y), size, (0,0,0), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img, (x,y), size, (b,g,r), -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        erasing = True
        cv.circle(img, (x,y), size, (0,0,0), -1)
    elif event == cv.EVENT_RBUTTONUP:
        erasing = False
        cv.circle(img, (x,y), size, (0,0,0), -1)
        
        

while(1):
    r = cv.getTrackbarPos("R", "canvas")
    g = cv.getTrackbarPos("G", "canvas")
    b = cv.getTrackbarPos("B", "canvas")
    size = cv.getTrackbarPos("Pen", "canvas")
    img[0:24, 0:24] = [b,g,r]
    cv.setMouseCallback("canvas", draw)
    cv.imshow("canvas", img)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break
