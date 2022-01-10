import cv2 as cv
import numpy as np

img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Me.jpg")
cv.imshow("Me.jpg", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

print(blank.shape)
print(img.shape)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), img.shape[1]//2, (255,255,255), -1)
cv.imshow("Mask", mask)

mask = cv.bitwise_not(mask)

maskedimg = cv.bitwise_and(mask,img)
cv.imshow("Masked", maskedimg)

cv.waitKey(0)
cv.destroyAllWindows()
