"""
import cv2
import numpy as np
FILE_NAME = cv2.imread("apple.jpg",cv2.IMREAD_GRAYSCALE)
 
img_changed = cv2.resize(FILE_NAME, (600, 500), interpolation= cv2.INTER_CUBIC)

cv2.imshow('cubic.jpg',img_changed)
cv2.waitKey(0)
"""
"""
 #nearest
import cv2
import numpy as np

FILE_NAME = cv2.imread("apple.jpg",cv2.IMREAD_GRAYSCALE)
 
img_changed = cv2.resize(FILE_NAME, (600, 500), interpolation= cv2.INTER_NEAREST)

cv2.imshow('nearest.jpg',img_changed)
cv2.waitKey(0)
"""
#linear

import cv2
import numpy as np


FILE_NAME = cv2.imread("apple.jpg",cv2.IMREAD_GRAYSCALE)
 
img_changed = cv2.resize(FILE_NAME, (600, 500), interpolation= cv2.INTER_LINEAR)

cv2.imshow('linear.jpg',img_changed)
cv2.waitKey(0)