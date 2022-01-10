import cv2 as cv
import numpy as np
import time
from mss import mss
from PIL import Image

# Going to be assuming 30 FPS so initialize array of zeros for 2 minutes worth of space. 

# We now have a working baseline product. It took a few hours of debugging small issues but now we have a good understanding of what's going on.

#capture = cv.VideoCapture(1)
#success,image  = capture.read()

# We have an app start logged right away to a path for us to save the video.
start = time.time()
path = "/Users/brockdonahue/Desktop/OpenCVBootCamp/videos/" + str(start) + ".mp4"

# First improvement can be creating an object to structure all of the code, firstly we have a main and replay function

# replay is to be called after any amount of time of the main function running, it can then save the last two minutes of recorded time or continue recording
def replay(cache, iterations):
    global path
    display = np.zeros((1500,1500), dtype="uint8")
    save = 'press "s" to save video or "c" to continue recording'
    cv.putText(display,save,(10,750), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv.imshow("Recorded Video",display)
    key = cv. waitKey(0)
    if key & 0xFF == 27:
        cv.destroyAllWindows()
    elif key == ord("s"):

        out = cv.VideoWriter(path, 0x7634706d, 30.0, (cache[0].shape[1], cache[0].shape[0]))
        print((cache[0].shape[1],cache[0].shape[0]))
        for frame in cache:
            out.write(frame)
            cv.imshow("Recorded Video",frame)
            if cv.waitKey(33) & 0xFF == 27:
                break
    elif key == ord("c"):
        cv.destroyWindow("Recorded Video")
        main(iterations+1, cache)
        

# The main function is handling the screen grabs of our program and processes it into a usable format to be recorded later, could handle the file changing later if it seems beneficial
def main(iterations=1, cache=[]):
    sct = mss()
    frames = len(cache)
    current = 0
    prev = 0
    capturingScreen = True
    bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    # initialize all our parameters and then start capturing the screen
    while capturingScreen:
        #success,img = capture.read()
        screenshot = sct.grab(bounding_box)
        img = np.array(screenshot)
        desired_image = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
        current= time.time()
        fps = int(1/(current-prev))
        frames += 1
        prev = current

        if frames >= 3600:
            cache.pop(0)
        
        cache.append(desired_image)
        print(fps)
        
        blank = np.zeros((1500,1500), dtype=np.uint8)
        text = 'hit "r" to see recorded video, or escape to end program'
        runs = str(iterations)
        cv.putText(blank,text,(10,750),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
        cv.putText(blank,runs,(10,850),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
        cv.imshow("Image",blank)
        keyPressed = cv.waitKey(33)
        if keyPressed & 0xFF == 27:
            break
        elif keyPressed == ord("r"):
            capturingScreen = False
            replay(cache, iterations)
    cv.destroyAllWindows()

main()

   

