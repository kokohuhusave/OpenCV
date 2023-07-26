import cv2
import matplotlib.pyplot as plt
import numpy as np

src1 = cv2.imread('./flowers.jpg')
src2 = cv2.imread('./pink.jpg')

alpha = 0.7

dst1 = src1 * alpha + src2 * (1-alpha)
dst1 = dst1.astype(np.uint8)

dst2 = dst1.addWeighted(src1, alpha, src2, (1-alpha), 0)

img = {'src1': src1, 'scr2': src2, 'dst1': dst1, 'dst2': dst2}

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()