import cv2 as cv

img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Me.jpg")
cv.imshow("Basic Me", img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

cv.waitKey(0)
cv.destroyAllWindows()