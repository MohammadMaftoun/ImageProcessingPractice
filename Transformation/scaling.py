import cv2
import numpy as np
FILE_NAME = 'Penguin.png'
cv2.imshow('ORG: ', cv2.imread("Penguin.png"))
img = cv2.imread(FILE_NAME)
(height, width) = img.shape[:2]
res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
cv2.imshow('Image: ', res)
cv2.waitKey(0)
