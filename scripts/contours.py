import cv2 as cv
import numpy as np

img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Me.jpg")
cv.imshow("Basic Me", img)

blank1 = np.zeros(img.shape, dtype="uint8")
blank2 = np.zeros(img.shape, dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# canny edges does everything i slaved over for hours in CMPEN 454, but better...
# threshold values are min and max values that we say are "significant"
# the picture im using here has really poor edge contrast on my facial features so we need a lower max value, this introduces more edge noise though.
# Just one way to get countours by doing canny edges and taking contours and hierarchy
canny = cv.Canny(gray, 75, 150)
cv.imshow("Canny", canny)

contours1, hierarchy1 = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours1))

# here we use threshold method, takes a grayscale image and threshold values.
# Can use adaptive thresholds to help ensure we recover the desired information (edges).
# first threshold value is what we compare pixel values to and second value is what we assign those that pass to.
ret, thresh = cv.threshold(gray, 75, 255, cv.THRESH_BINARY)

contours2, hierarchy2 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours2))

cv.imshow("thresh", thresh)

drawncontours1 = cv.drawContours(blank1, contours1, -1, (0, 255, 0), 2)
drawnContours2 = cv.drawContours(blank2, contours2, -1, (0, 0, 255), 2)
cv.imshow("Drawn Controus 1", drawncontours1)
cv.imshow("Drawn Contours 2", drawnContours2)
 
cv.waitKey(0)
cv.destroyAllWindows()