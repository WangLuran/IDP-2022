import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

from photo _capture import PullFrameFromStream

def camera_calibrate(img):
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((7*7,3), np.float32)
    objp[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)

    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    
    if type(img) != np.array:
        img = np.array(img)
        
    img = np.array(img)
    #gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(img, (7,7), None)
    print(ret)
    
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        corners2 = cv.cornerSubPix(gray,corners,(5,5),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        '''plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB), cmap='gray')
        plt.scatter(corners2[:, 0, 0], corners2[:, 0, 1])
        plt.show()'''
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
    print(mtx, dist)
    path = "calibration_chessboard.yml"
    save_coefficients(mtx, dist, path)
    h,  w = img.shape[:2]
    print(h, w)
    newcameramtx, roi=cv.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
    dst = cv.undistort(img, mtx, dist, None, newcameramtx)
    
    print("dst done")
    
def save_coefficients(mtx, dist, path):
    '''Save the camera matrix and the distortion coefficients to given path/file.'''
    cv_file = cv.FileStorage(path, cv.FILE_STORAGE_WRITE)
    cv_file.write('K', mtx)
    cv_file.write('D', dist)
    # note you *release* you don't close() a FileStorage object
    cv_file.release()

def load_coefficients(path):
    '''Loads camera matrix and distortion coefficients.'''
    # FILE_STORAGE_READ
    cv_file = cv.FileStorage(path, cv.FILE_STORAGE_READ)

    # note we also have to specify the type to retrieve other wise we only get a
    # FileNode object back instead of a matrix
    camera_matrix = cv_file.getNode('K').mat()
    dist_matrix = cv_file.getNode('D').mat()

    cv_file.release()
    return [camera_matrix, dist_matrix]
    
img = PullFrameFromStream()

camera_calibrate(img)

