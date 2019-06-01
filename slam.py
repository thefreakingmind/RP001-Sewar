import numpy 
import cv2 
import sdl2.ext 
import sdl2
from display import Display




W = 1920//2
H = 1080//2

sdl2.ext.init()

dis = Display(W,H)


class FeatureExtractor(object):
    # TODO Write a Feature Extractor
    
    pass




def process_frame(img):
    img = cv2.resize(img ,(W,H))
    dis.draw(img)


if __name__ == '__main__':
    cap = cv2.VideoCapture('test.mp4')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break

    exit(0)
