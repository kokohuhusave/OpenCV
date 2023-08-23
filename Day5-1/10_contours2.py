import cv2
import random

# 이미지 파일 경로
img_path = './image/milkdrop.bmp'

# 'Malgun Gothic' 폰트를 사용하여 한글 지원
font_path = 'C:/Windows/Fonts/malgun.ttf'
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# 이미지 처리를 위해 가우시안 블러와 캐니 에지 검출을 적용합니다.
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
edges = cv2.Canny(blurred_img, 30, 150)

# 에지 검출된 이미지에서 윤곽선을 검출합니다.
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 윤곽선을 그리기 위해 새로운 빈 이미지를 생성합니다.
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# 랜덤한 색상으로 윤곽선을 그립니다.
for contour in contours:
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, [contour], -1, color, 3)

# 윈도우에 이미지 출력
cv2.imshow('원본 이미지', img)
cv2.imshow('에지 검출', edges)
cv2.imshow('외곽선 추출 결과', dst)
cv2.waitKey()