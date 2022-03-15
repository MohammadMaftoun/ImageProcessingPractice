# Equalization
import cv2
import numpy as np
from matplotlib import pyplot as plt
FILE_NAME = cv2.imread('nature.jpg',cv2.IMREAD_GRAYSCALE)
Histogram = cv2.calcHist([FILE_NAME],[0],None,[256],[0,256])
Equalize = cv2.equalizeHist(FILE_NAME)
Stacking = np.hstack((FILE_NAME, Equalize))
HI=cv2.equalizeHist(Stacking)
cv2.imshow('output.png', HI)
Result_equ=cv2.calcHist([Equalize],[0],None,[256],[0,256])
plt.plot(Histogram)
plt.plot(Result_equ);plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

