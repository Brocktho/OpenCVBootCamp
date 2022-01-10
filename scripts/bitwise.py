import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype=np.uint8)

rect = cv.rectangle(blank.copy(),(30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rect)
cv.imshow("Circle", circle)

# Bitwise and operation, can be an easy mask
bitand = cv.bitwise_and(rect,circle)
cv.imshow("Bitand", bitand)

# Bitwise or operation
bitor = cv.bitwise_or(rect,circle)
cv.imshow("Bitor", bitor)

# Bitwise Xor operation, exclusive or
bitxor = cv.bitwise_xor(rect,circle)
cv.imshow("Bitxor", bitxor)

# Bitwise Not operation
bitnot = cv.bitwise_not(rect)
cv.imshow("Bitnot", bitnot)


cv.waitKey(0)
cv.destroyAllWindows()
