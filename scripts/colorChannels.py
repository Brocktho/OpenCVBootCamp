import cv2 as cv
import numpy as np

img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Me.jpg")
cv.imshow("Me", img)

b,g,r = cv.split(img)

# shows gray scale since we are in a 1 channel mode, if we create a blank 3 channel image and add our respective channel we can see the true colors.
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red",r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge(b,g,r)


cv.waitKey(0)
cv.destroyAllWindows()