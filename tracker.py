import numpy as np
import os
from kalman_filter import KalmanFilter
from scipy.optimize import linear_sum_assignment
from datetime import datetime
import pandas as pd
import math

class Track(object):
    def __init__(self, prediction, trackIdCount):
        self.track_id = trackIdCount  
        self.KF = KalmanFilter()  
        self.prediction = np.asarray(prediction)  
        self.skipped_frames = 0  
        self.trace = []   
        self.start_time = datetime.utcnow()
        self.track = [] 
        self.passed = False
        self.value = False

class Tracker(object):
    def __init__(self, dist_thresh, max_frames_to_skip, max_trace_length,
                 trackIdCount):
        self.dist_thresh = dist_thresh
        self.max_frames_to_skip = max_frames_to_skip
        self.max_trace_length = max_trace_length
        self.tracks = []
        self.trackIdCount = trackIdCount
        self.initial_count = 20
        self.p0 = np.zeros((2,3))
        self.p1 = np.zeros((1,2))
        self.n = 200
        self.exc_val = []
        

        
    def update(self, detections):
        if len(self.tracks) == 0:
            for i in range(len(detections)):
                track = Track(detections[i], self.trackIdCount)
                self.trackIdCount += 1
                self.tracks.append(track)


        N = len(self.tracks)
        M = len(detections)
        cost = np.zeros(shape=(N, M))   # Cost matrix
        for i in range(len(self.tracks)):
            for j in range(len(detections)):
                try:
                    diff = self.tracks[i].prediction - detections[j]
                    # Calculating The Difference in Each Frame
                    distance = np.sqrt(diff[0]*diff[0] +
                                       diff[1]*diff[1])
                    cost[i][j] = distance
                except Exception as e:
                    print(e)

        cost = (0.5) * cost

        assignment = [-1 for _ in range(N)]
        row_ind, col_ind = linear_sum_assignment(cost)
        for i in range(len(row_ind)):
            assignment[row_ind[i]] = col_ind[i]
        un_assigned_tracks = []
        for i in range(len(assignment)):
            if assignment[i] != -1:
                if cost[i][assignment[i]] > self.dist_thresh:
                    assignment[i] = -1
                    un_assigned_tracks.append(i)
                pass
            else:
                self.tracks[i].skipped_frames += 1

        del_tracks = [i for i in range(len(self.tracks)) if self.tracks[i].skipped_frames > self.max_frames_to_skip]
        if len(del_tracks) > 0:  # only when skipped frame exceeds max
            for id in del_tracks:
                if id < len(self.tracks):
                    del self.tracks[id]
                    del assignment[id]
                else:
                    print("ERROR: id is greater than length of tracks")

        un_assigned_detects = [i for i in range(len(detections)) if i not in assignment]
        if len(un_assigned_detects) != 0:
            for i in range(len(un_assigned_detects)):
                track = Track(detections[un_assigned_detects[i]],
                              self.trackIdCount)
                self.trackIdCount += 1
                self.tracks.append(track)

        for i in range(len(assignment)):
            self.tracks[i].KF.predict()

            if assignment[i] != -1:
                self.tracks[i].skipped_frames = 0
                self.tracks[i].prediction = self.tracks[i].KF.correct(
                                            detections[assignment[i]], 1)
            else:
                self.tracks[i].prediction = self.tracks[i].KF.correct(
                                            np.array([[0], [0]]), 0)

            if len(self.tracks[i].trace) > self.max_trace_length:
                for j in range(len(self.tracks[i].trace) -
                               self.max_trace_length):
                    del self.tracks[i].trace[j]

            self.tracks[i].trace.append(self.tracks[i].prediction)
            self.tracks[i].KF.lastResult = self.tracks[i].prediction
