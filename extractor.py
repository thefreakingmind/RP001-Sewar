import numpy as np
import cv2 
import sdl2.ext 
import sdl2
from skimage.transform import FundamentalMatrixTransform
from skimage.feature import match_descriptors, ORB, plot_matches


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
        matches = self.bf.knnMatch(kps, des, k=2) 
        last = {'des':des, 'kps':kps}
            
        for m in kps:
            print(m.pt)
        return kps,des, matches

    def match():
        pass


