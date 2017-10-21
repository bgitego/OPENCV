import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('POINT_Index/Capture_1.PNG',0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
