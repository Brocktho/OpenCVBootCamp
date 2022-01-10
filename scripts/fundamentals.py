import cv2 as cv

# Reading in an Image
img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Me.jpg")
cv.imshow("Basic Me", img)

# Converting to Gray Scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale", gray)

# Blurring Image, apply gaussian with given kernel size
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blur)

# Edging Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Edged", canny)

# Dilating after edging (increase width of edges)
dilated = cv.dilate(canny, (5,5), iterations=2)
cv.imshow("Dilated", dilated)

# Recover image by Eroding (decrease width of edges)
eroded = cv.erode(dilated, (5,5), iterations=2)
cv.imshow("Eroded", eroded)

cv.waitKey(0)
cv.destroyAllWindows()