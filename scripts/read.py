import cv2 as cv

# Reading in an Image
#img = cv.imread("/Users/brockdonahue/Desktop/OpenCVBootCamp/images/Download.jpeg")
#cv.imshow("Meme", img)

capture = cv.VideoCapture("/Users/brockdonahue/Desktop/OpenCVBootCamp/videos/1641250935.982923.mp4")

def resizeFrame(frame, scale=0.75):
    # Works with images, video files and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#def changeResolution(width, height):
    # Works with live video, don't care for this one much
    #capture.set(3, width)
    #capture.set(4, height)

#newimage = resizeFrame(img, 0.5)
#cv.imshow("Rescaled Meme", newimage)

# Reading in a Video, Integer for cameras on computer, or filepath
#capture = cv.VideoCapture("/Users/brockdonahue/Desktop/OpenCVBootCamp/videos/CrapMeme.mp4")

# For videos, while loop to go through all frames

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video",frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # If d is pressed break out of video
        break

#capture.release()
cv.waitKey(0)
cv.destroyAllWindows()