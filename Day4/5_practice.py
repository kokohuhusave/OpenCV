import cv2
import numpy as np

# 원의 초기 좌표를 설정합니다.
center = (0,0)
radius = 50
color = (255, 255, 0)
thickness = -1

def draw_circle(event, x, y, flags, param):
    global center
    if event == cv2.EVENT_LBUTTONDOWN:
        # 마우스를 클릭하면, 원의 중심을 마우스의 위치로 업데이트합니다.
        center = (x, y)
        # 새로운 위치에 원을 그립니다.
        img[:] = original_img[:]
        cv2.circle(img, center, radius, color, thickness)

# 원본 이미지를 로드합니다.
original_img = cv2.imread('./namecard.jpg')

# 원본 이미지의 복사본을 만듭니다. 이 이미지에 원을 그립니다.
img = original_img.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_circle)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
