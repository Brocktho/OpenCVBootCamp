import cv2 as cv
import numpy as np
import time

start = time.time()

class Capture():
    # requires a capture type to be sent into recorder, if not does not work properly.
    def __init__(self, path: str="/Users/brockdonahue/Desktop/OpenCVBootCamp/videos/" + str(start) + ".mp4", maxCache: int=3600, recorder = None):
        self.path = path
        self.maxCache = maxCache
        self.cache = []
        self.capturing = False
        self.viewingCache = False
        self.playingCache = False
        self.editingFrame = False
        self.drawing = False
        self.erasing = False
        self.saving = False
        self.framenum = 0
        self.iterations = 1
        self.r = 0
        self.g = 0
        self.b = 0
        self.size = 1
        self.frame = None
        self.recorder = recorder
    

    def save(self):
        cv.destroyAllWindows()
        self.saving = True
        display = np.zeros((1500,1500), dtype="uint8")
        save = 'press "s" to save video or "c" to continue recording'
        cv.putText(display,save,(10,750), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
        cv.imshow("Recorded Video",display)
        key = cv. waitKey(0)
        if key & 0xFF == 27:
            cv.destroyAllWindows()
        elif key == ord("s"):
            out = cv.VideoWriter(self.path, 0x7634706d, 30.0, (self.cache[0].shape[1], self.cache[0].shape[0]))
            for framenum,frame in enumerate(self.cache):
                print("currently writing frame: " + str(framenum) + "  out of " + str(len(self.cache)) + " total frames.")
                out.write(frame)
                if cv.waitKey(33) & 0xFF == 27:
                    self.terminate()
            # After saving reset settings and begin the process again since we can escape to terminate early.
            self.cache = []
            self.iteration = 1
            self.recorder()
        elif key == ord("c"):
            cv.destroyWindow("Recorded Video")
            self.iterations += 1
            self.recorder()
        

    # viewing cache should always be an option so we extend it to parent class, now need to accept a recording type in place of backgroundRecording
    def viewCache(self):
        cv.destroyAllWindows()
        self.framenum = 0
        self.viewingCache = True
        self.playingCache = True
        while self.viewingCache:
            # Have now made a somewhat happy recording software, can pause, play, skip forward a second or go frame by frame.
            while self.playingCache:
                if self.framenum >= len(self.cache):
                    self.framenum = len(self.cache) - 1
                cv.imshow("Recorded Video", self.cache[self.framenum])
                key = cv.waitKey(33)
                # quit out at any time with escape
                if key & 0xFF == 27:
                    self.terminate()
                # quick and dirty way to skip ahead 30 frames (1 second assuming 30 fps though i haven't been recording that quickly yet...)
                elif key == ord("a"):
                    if self.framenum >=30:
                        self.framenum -= 30
                    else:
                        self.framenum = 0
                elif key == ord("d"):
                    self.framenum += 30
                # go frame by frame forward
                elif key == ord(","):
                    self.playingCache = False
                    self.framenum -= 1
                elif key == ord("."):
                    self.playingCache = False
                    self.framenum += 1
                # spacebar go pause, makes frame by frame work better, gonna add frame by frame pauses the video actually...
                elif key == 32:
                    self.playingCache = False
                # c allows you to go back to recording the video.
                elif key == ord("c"):
                    self.iterations += 1
                    self.recorder()
                    self.viewingCache = False
                # p lets you edit the current frame of the video
                elif key == ord("p"):
                    self.viewingCache = False
                    self.playingCache = False
                    self.editFrame()
                elif key == ord("r"):
                    self.viewingCache = False
                    self.playingCache = False
                    self.save()
                self.framenum += 1  
            if self.framenum >= len(self.cache):
                self.framenum = len(self.cache) - 1
            cv.imshow("Recorded Video", self.cache[self.framenum])
            key = cv.waitKey(33)
            if key & 0xFF == 27:
                self.terminate()
            elif key == ord("a"):
                if self.framenum >=30:
                    self.framenum -= 30
                else:
                    self.framenum = 0
            elif key == ord("d"):
                self.framenum += 30
            elif key == ord(","):
                self.framenum -= 1
            elif key == ord("."):
                self.framenum += 1
            elif key == ord("p"):
                self.viewingCache = False
                self.editFrame()
            elif key == 32:
                self.playingCache = True
            elif key == ord("r"):
                    self.viewingCache = False
                    self.save()
            elif key == ord("c"):
                self.iterations += 1
                self.recorder()
                self.viewingCache = False


    def nothing(self,**args):
        pass

    
    def editFrame(self):
        cv.destroyAllWindows()
        self.editingFrame = True
        self.frame = self.cache[self.framenum]
        cv.namedWindow("canvas")
        # this part of the program isn't super performant, might remove for now cause while cool it doesn't really work as I want.
        cv.createTrackbar("R", "canvas", 0, 255, self.nothing)
        cv.createTrackbar("B", "canvas", 0, 255, self.nothing)
        cv.createTrackbar("G", "canvas", 0, 255, self.nothing)
        cv.createTrackbar("Pen", "canvas", 0, 64, self.nothing)
        while self.editingFrame:
            self.r = cv.getTrackbarPos("R", "canvas")
            self.g = cv.getTrackbarPos("G", "canvas")
            self.b = cv.getTrackbarPos("B", "canvas")
            self.size = cv.getTrackbarPos("Pen", "canvas")
            self.frame[0:24, 0:24] = [self.b, self.g, self.r]
            cv.setMouseCallback("canvas", self.draw)
            cv.imshow("canvas", self.frame)
            k = cv.waitKey(20) & 0xFF
            if k == 27:
                self.terminate()
            elif k == ord('c'):
                self.iterations += 1
                self.recorder()


    # draw used for mouse event handling on frames. not performant on my computer unsure of other devices...
    def draw(self, event, x, y, flags, params):
        if event == cv.EVENT_LBUTTONDOWN:
            self.drawing = True
            cv.circle(self.frame, (x,y), self.size, (self.b, self.g, self.r), -1)
        elif event == cv.EVENT_MOUSEMOVE:
            if self.drawing:
                cv.circle(self.frame, (x,y), self.size, (self.b, self.g, self.r), -1)
            elif self.erasing:
                cv.circle(self.frame, (x,y), self.size, (0,0,0), -1)
        elif event == cv.EVENT_LBUTTONUP:
            self.drawing = False
            cv.circle(self.frame, (x,y), self.size, (self.b, self.g, self.r), -1)
        elif event == cv.EVENT_RBUTTONDOWN:
            self.erasing = True
            cv.circle(self.frame, (x,y), self.size, (0,0,0), -1)
        elif event == cv.EVENT_RBUTTONUP:
            self.erasing = False
            cv.circle(self.frame, (x,y), self.size, (0,0,0), -1)


    def terminate(self):
        cv.destroyAllWindows()
        self.capturing = False
        self.viewingCache = False
        self.playingCache = False
        self.editingFrame = False
        self.drawing = False
        self.erasing = False
        self.saving = False
