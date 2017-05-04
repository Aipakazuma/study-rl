# -*- coding: utf-8 -*-
import numpy as np
import cv2
import glob,os


def prepare():
    # prepare object points
    nx = 9 #TODO: enter the number of inside corners in x
    ny = 5 #TODO: enter the number of inside corners in y

    # Make a list of calibration images
    images = glob.glob('camera_cal/calibration*.jpg')

    objpoints = []
    imgpoints =[]

    objp = np.zeros((9*5,3),np.float32)
    objp[:,:2] = np.mgrid[0:9,0:5].T.reshape(-1,2)

    for frame in images:
        img = cv2.imread(frame)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Find the chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
        # If found, draw corners
        if ret == True:
            # Draw and display the corners
            imgpoints.append(corners)
            objpoints.append(objp)
            cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    return objpoints, imgpoints 


if __name__ == '__main__':
    objpoints, imgpoints = prepare()
