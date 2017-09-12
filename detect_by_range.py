import cv2
import numpy as np

img = cv2.imread('ex2.png')
cimg = cv2.imread('ex2.png')

color = img[250, 220]
cv2.circle(cimg, (250, 220), 2, (0, 0, 255), 3)
print color

cv2.imshow('rgb', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()