import numpy as np
import matplotlib.pyplot as plt
import cv2 
from numpy import linspace, loadtxt, ones, convolve
import numpy as np
import pandas as pd
import collections
import scipy as sp
from collections import defaultdict

class KalmanFilter(object):
    def __init__(self):
        self.dt = 0.005 
        self.A = np.array([[1, 0], [0, 1]]) 
        self.u = np.zeros((2, 1)) 
        self.b = np.array([[0], [255]])  
        self.P = np.diag((3.0, 3.0)) 
        self.F = np.array([[1.0, self.dt], [0.0, 1.0]]) 
        self.inference = np.zeros((2,3))
        self.Q = np.eye(self.u.shape[0]) 
        self.R = np.eye(self.b.shape[0])  
        self.lastResult = np.array([[0], [255]])
        self.value = 100.0

    def moving_average(self, data,  window):
        self.window = np.ones(int(window_size))/(float(window_size))
        return np.convolve(self.data, self.window, 'same') 

    
    def predict(self):
        self.u = np.round(np.dot(self.F, self.u))
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + self.Q
        self.lastResult = self.u
        self.x_value  = 0
        return self.u * self.x_value* self.value

    def correct(self, b, flag):
        if not flag:  
            self.b = self.lastResult
        else: 
            self.b = b
        C = np.dot(self.A, np.dot(self.P, self.A.T)) + self.R
        K = np.dot(self.P, np.dot(self.A.T, np.linalg.inv(C)))
        self.u = np.round(self.u + np.dot(K, (self.b - np.dot(self.A,
                                                              self.u))))
        self.P = self.P - np.dot(K, np.dot(C, K.T))
        self.lastResult = self.u
        return self.u
