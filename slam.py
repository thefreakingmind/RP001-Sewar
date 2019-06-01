import numpy as np
import cv2 
import sdl2.ext 
import sdl2
from display import Display




W = 1920//2
H = 1080//2

sdl2.ext.init()

dis = Display(W,H)

class FeatureExtractor(object):
    def __init__(self):
        self.orb = cv2.ORB_create()


    # Extracting Features
    def extract(self, img):
        kp, des = self.orb.detectAndCompute(img, None)
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000,qualityLevel=0.01, minDistance=3)
        kps = [cv2.KeyPoint(x=f[0][0],y=f[0][1], _size=20) for f in feats]
        for m in kps:
            print(m.pt)
        return feats


def process_frame(img):
    img = cv2.resize(img ,(W,H))
    feature = FeatureExtractor()
    kp = feature.extract(img)
    for p in kp:
        u,v = map(lambda x: int(round(x)),p[0])
        cv2.circle(img, (u,v), color=(0, 255, 0), radius=3)
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
