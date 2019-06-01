import numpy as np
import cv2 
import sdl2.ext 
import sdl2

# Feature Extractor
class FeatureExtractor(object):
    def __init__(self):
        self.orb = cv2.ORB_create()
        self.last = None
        self.bf = cv2.BFMatcher

    # Extracting Features
    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000,qualityLevel=0.01, minDistance=3)
        kps = [cv2.KeyPoint(x=f[0][0],y=f[0][1], _size=20) for f in feats]
        kps, des = self.orb.compute(img, kps)
        if self.last is not None:
            match = self.bf.BF 
            
        for m in kps:
            print(m.pt)
        return kps,des


