import numpy as np
import cv2 as cv

img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Me.jpg")

cv.imshow("Basic Me", img)

# translate the image -x -> left, +x -> right
# -y -> up,  +y -> down
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions =  (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 200, 50)
cv.imshow("Translated", translated)

# Rotate
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 30)
cv.imshow("Rotated", rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

# Flipping 0 = vertical flip, 1 = horizontal flip, -1 = vertical & horizontal
flipped = cv.flip(img, -1)
cv.imshow("Flipped", flipped)

# Cropping simply slice the image array
cropped = img[200:400, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
cv.destroyAllWindows()