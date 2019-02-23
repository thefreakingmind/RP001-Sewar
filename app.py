#Using CV2 to get Features
import numpy as np
import cv2
import sdl2.ext
import sdl2
from display import Display
orb = cv2.ORB_create()
W = 1920//2
H = 1080//2


disp = Display(W,H)

def process_frame(img):
    img = cv2.resize(img, (W,H))
    disp.draw(img)
    
    '''    
    kp, des = orb.detectAndCompute(img, None)
    for p in kp:
        u,v = map(lambda x: int(round(x)),p.pt)
        update = cv2.goodFeaturesToTrack(img,(u,v), color=(0,255,0), radius=3)
        cv2.imshow('Update',update)
        cv2.waitKey()
    #print(img.shape)
    #print(img)
    #print(pygame.surfarray.array2d(img))
    '''

if __name__ == '__main__':
    cap = cv2.VideoCapture('test.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            exit(0)

