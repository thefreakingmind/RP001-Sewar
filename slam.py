import numpy as np
import cv2 
import sdl2.ext 
import sdl2
from display import Display
from extractor import FeatureExtractor

W = 1920//2
H = 1080//2

sdl2.ext.init()

dis = Display(W,H)
feature = FeatureExtractor()

def process_frame(img):
    img = cv2.resize(img ,(W,H))
    kp, des, match = feature.extract(img)
    for m in match:
        print(m)
    for p in kp:
        u,v = map(lambda x: int(round(x)),p.pt)
        cv2.circle(img, (u,v), color=(255, 0, 0), radius=3)
    dis.draw(img)


if __name__ == '__main__':
    cap = cv2.VideoCapture('joke.mp4')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break

    exit(0)
