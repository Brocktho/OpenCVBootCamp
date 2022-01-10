import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Me.jpg")
cv.imshow("Me.jpg", img)

# histograms can be grayscale or RGB
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blank = np.zeros(gray.shape, dtype="uint8")

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 250, 255, -1)

maskedimage = cv.bitwise_and(mask,gray)
cv.imshow("maskedimage", maskedimage)

# grayscale histogram
gray_hist = cv.calcHist([gray], [0], maskedimage, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()