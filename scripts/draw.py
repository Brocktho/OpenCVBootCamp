import cv2 as cv
import numpy as np

# Initialize 500 x 500 pixels with 3 color channels
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("blank", blank)

# Manual painting across the screen, b g r channels [0, 255, 0]
blank[150:300, 200:400] = 0,0,255
blank[50:120, 120:190] = 255, 0, 0
cv.imshow("Red & Blue Shapes", blank)

# cv rectangle method, takes image, two points, and optionals for style
cv.rectangle(blank, (0,0), (200, 250), (0,255,0), thickness=2)
cv.imshow("Red & Blue with green rectangle", blank)

# cv circle method, takes a point and a radius
cv.circle(blank, (350, 350), 40, (255,0,0), thickness=-1)
cv.imshow("Circle added", blank)

# cv line method, takes two points
cv.line(blank, (120,120), (250, 250), (255, 255, 255), thickness=3)
cv.imshow("Line added", blank)

# cv putText method, takes image, text you want, location to start at
cv.putText(blank, "Hello World", (20, 250), cv.FONT_HERSHEY_SIMPLEX, 2, (0,255,0))
cv.imshow("text added", blank)

cv.waitKey(0)
cv.destroyAllWindows()

