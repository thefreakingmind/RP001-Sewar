import numpy as np
import cv2 
import sdl2.ext
sdl2.ext.init()
orb = cv2.ORB_create()
W = 1920//2
H = 1080//2


window = sdl2.ext.Window("SLAM", size=(W,H))
window.show()


def process_frame(img):
    img = cv2.resize(img, (W,H))
    events = sdl2.ext.get_events()
    for events in events:
        if events.type==sdl2.SDL_QUIT:
            running=False
    #kp, des = orb.detectAndCompute(img, None)
    #for p in kp:
    #    u,v = map(lambda x: int(round(x)), p.pt)
    #    update = cv2.circle(img, (u,v), color=(0,255,0), radius=4)
    #    cv2.imshow('Image', update)
    window.refresh()
    print(img)



if __name__ == '__main__':
    cap = cv2.VideoCapture('Crap.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            process_frame(frame)

        else:
            exit(0)

