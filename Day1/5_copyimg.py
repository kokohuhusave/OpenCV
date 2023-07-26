import cv2

img_origin = cv2.imread('./dog.bmp')
'''

img_origin = img_origin[91:125 , 125:245] # H, W
img_copy = img_origin

cv2.imshow('img_origin', img_origin)
cv2.imshow('img_copy', img_copy)
cv2.waitKey()
'''
img_copy = img_origin[91:125 , 125:245].copy()

cv2.imshow('img_origin', img_origin)
cv2.imshow('img_copy', img_copy)
cv2.waitKey()
