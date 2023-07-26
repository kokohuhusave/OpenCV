# dog.bmp 이미지를 사용하여 3채널(RGB)로 계싼해 히스토그램 그리기
# 단 하나의 그래프 그리기
import cv2
import matplotlib.pyplot as plt
import sys
src = cv2.imread('./dog.bmp')

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey(1)

plt.show()