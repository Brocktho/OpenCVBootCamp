import cv2 as cv

img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Me.jpg")
cv.imshow("Me", img)

# regular blur
average = cv.blur(img, (3,3))
cv.imshow("average", average)

# gaussian blur
gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow("gauss", gauss)

# median blur, a bit better at getting rid of salt and pepper noise
median = cv.medianBlur(img,3)
cv.imshow("median", median)

#Bilateral blur maintains edges
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)
cv.destroyAllWindows()