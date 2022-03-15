import cv2
import numpy as np
FILE_NAME = 'Penguin.png'
cv2.imshow('ORG: ', cv2.imread("Penguin.png"))
M = np.float32([[1, 0, 100], [0, 1, 50]])
img = cv2.imread(FILE_NAME)
(rows, cols) = img.shape[:2]
res = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Image: ', res)
cv2.waitKey(0)
