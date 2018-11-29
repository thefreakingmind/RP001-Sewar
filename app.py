#Using CV2 to get Features
import numpy as np
import cv2
import sdl2.ext
import sdl2
#import pygame

orb = cv2.ORB_create()
W = 1920//2
H = 1080//2
#pygame.init()
#display = pygame.display.set_mode((W,H))
#sdl2.ext.init()
#window = sdl2.ext.Window("Hello World!", size=(W, H), position=(-500, 500))
#window.show()


def process_frame(img):
    #kp = orb.detect(img, None)
    img = cv2.resize(img, (W,H))
    #events = sdl2.ext.get_events()
    #for events in events:
    #    if events.type == sdl2.SDL_QUIT:
    #        exit(0)
    #window.refresh()
    kp, des = orb.detectAndCompute(img, None)
    for p in kp:
        u,v = map(lambda x: int(round(x)),p.pt)
        update = cv2.circle(img,(u,v), color=(0,255,0), radius=3)
        cv2.imshow('Update',update)
        cv2.waitKey(2)
    #print(img.shape)
    #print(img)
    #print(pygame.surfarray.array2d(img))


if __name__ == '__main__':
    cap = cv2.VideoCapture('Crap.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            exit(0)

