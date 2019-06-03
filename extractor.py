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

    
    def extract(self, img):
        val = []
        # Detection 
        feats = cv2.goodFeaturesToTrack(
                np.mean(img, axis=2).astype(np.uint8), 
                3000,qualityLevel=0.01,
                minDistance=3)
        
        # Extraction 
        kps = [cv2.KeyPoint(x=f[0][0],y=f[0][1], _size=20) 
                for f in feats]
        kps, des = self.orb.compute(img, kps)
                for kp in kps:
            print(kp.pt)
        return kps,des

    
    def match(self):
        # Matching

        # TODO Implement Matching Algorithm and Remove
        # Noise in the Video
        matches = None
        if self.last is not None:
           matches = self.bf.match(des, self.last['des']) 
        
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                val.append([m])
                
        
        self.last = {'des':des, 'kps':kps}

        return matches

