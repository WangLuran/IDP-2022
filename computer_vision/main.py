import cv2 as cv
import numpy as np

from camera_calibrate import camera_calibration
from image_processing import image_process
from calibration_coefficients import load_coefficients
from k_means import k_means
from photo_capture import PullFrameFromStream

img = PullFrameFromStream()
mtx, dist = load_coefficients('calibration_chessboard.yml')
img = np.array(img)
h,  w = img.shape[:2]
newcameramtx, roi=cv.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
x,y,w,h = roi
img = dst[y:y+h, x:x+w]
img = img[0:750, 0:450]
points, x_plot, y_plot = filter_image_np(img, block_RGB)
plt.scatter(points[:,0], points[:,1])
centroids = kmeans_open(points,3)
plt.scatter(centroids[:,0], centroids[:,1])
plt.show()
