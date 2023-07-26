import cv2
import matplotlib.pyplot as plt
import numpy as np

img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
print('img1 type: ', type(img_gray))
print('img1 shape: ', img_gray.shape) # img1 shape:  (364, 548) (height, width)
print('img1 dtype: ', img_gray.dtype) # img1 dtype:  uint8

img_color = cv2.imread('./dog.bmp')
print('img_color type: ', type(img_color))
print('img_color shape: ', img_color.shape)

# img_color의 가로 * 세로
print('img1 width * height: ', img_color.shape[0] * img_color.shape[1])
h, w = img_color.shape[:2]
print(f'img1 width * height: {h}*{w}')

# 그레이스케일 영상과 컬러 영상을 구별하는 방법
if len(img_gray.shape) == 2:
    print('img_gray는 그레이스케일입니다')
elif len(img_gray.shape) == 3:
    print('img_gray는 컬러 영상입니다')

# img_color에 특정 색 정보로 영상 출력
# BGR: (255, 102, 255)
'''
for x in range(h):
    for y in range(w):
        img_color[x, y] = (255, 102, 255)

cv2.imshow('img_color', img_color)
cv2.waitKey()
'''
'''
img_color[:,:] = (255, 102, 255)

cv2.imshow('img_color', img_color)
cv2.waitKey()
'''
