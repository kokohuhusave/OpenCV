# 가로, 세로 4등분하여 자동 이진화
import cv2
import numpy as np

# 이미지 불러오기
src = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)


# 이미지의 가로, 세로 길이
h, w = src.shape

# 이미지를 4등분하기 위한 중간 지점 계산
h_mid = h // 2
w_mid = w // 2

# 이미지를 4등분
src1 = src[:h_mid, :w_mid]
src2 = src[:h_mid, w_mid:]
src3 = src[h_mid:, :w_mid]
src4 = src[h_mid:, w_mid:]

# 각 부분에 대해 OTSU 이진화 적용
th1, dst1 = cv2.threshold(src1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th2, dst2 = cv2.threshold(src2, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th3, dst3 = cv2.threshold(src3, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th4, dst4 = cv2.threshold(src4, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print("otsu's threshold1:", th1)
print("otsu's threshold2:", th2)
print("otsu's threshold3:", th3)
print("otsu's threshold4:", th4)


dst = np.vstack((np.hstack((dst1, dst2)), np.hstack((dst3, dst4))))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
