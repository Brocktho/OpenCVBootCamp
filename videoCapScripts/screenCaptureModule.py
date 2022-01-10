import cv2 as cv
import numpy as np
import time
from mss import mss
from captureModule import Capture

# Going to be assuming 30 FPS so initialize array of zeros for 2 minutes worth of space. 

# We now have a working baseline product. It took a few hours of debugging small issues but now we have a good understanding of what's going on.

#capture = cv.VideoCapture(1)
#success,image  = capture.read()

# We have an app start logged right away to a path for us to save the video.
    #very surprising to me, turning it into modules like this seems to have improved performance? Paint feature still sucks tho...
class ScreenCapture(Capture):
    def __init__(self,screenSize=(1920, 1080), screenLocal=(0,0)):
        super().__init__(recorder = self.backgroundRecording)
        self.screenSize = screenSize
        self.screenLocal = screenLocal
        self.sco = mss()
    
    
    # First round of updates, realized with object class of Video Capture I can store my cache in the object and overwrite as necessary, just calling self.cache
    def backgroundRecording(self):
        # destroy all windows used for when the other pieces of the program were used and now returning to recording.
        cv.destroyAllWindows()
        current = 0
        prev = 0
        self.capturing = True
        bounding_box = {'top': 0, 'left': 0, 'width': self.screenSize[0], 'height': self.screenSize[1]}
        # initialize all our parameters and then start capturing the screen
        while self.capturing:
            frames = len(self.cache)
            #success,img = capture.read()
            screenshot = self.sco.grab(bounding_box)
            img = np.array(screenshot)
            desired_image = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
            current= time.time()
            fps = int(1/(current-prev))
            prev = current
            # warning to not lose data for the user, could make a one time update bool and have it flash a notification
            if frames >= int(self.maxCache*.9):
                print("Nearing max Cache size...")
            # designed for 2 minutes of playback at 30 FPS, can change to be higher or lower with an object variable
            if frames >= self.maxCache:
                self.cache.pop(0)

            self.cache.append(desired_image)

            print("current fps capture rate: " + str(fps))
            blank = np.zeros((1500,1500), dtype=np.uint8)
            text = 'hit "r" to record the video, hit "v" to view current recording, or escape to end program'
            runs = str(self.iterations)
            cv.putText(blank,text,(10,750),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
            cv.putText(blank,runs,(10,850),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
            cv.imshow("Image",blank)
            keyPressed = cv.waitKey(33)
            if keyPressed & 0xFF == 27:
                self.terminate()
            elif keyPressed == ord("r"):
                self.capturing = False
                self.save()
            elif keyPressed == ord("v"):
                self.capturing = False
                self.viewCache()
      

# main function to display the functionality of the module.
def main():
    # currently only records .mp4, filepath must end in .mp4 for it to function!
    screenCapture = ScreenCapture()
    screenCapture.backgroundRecording()

if __name__ == "__main__":
    main()
