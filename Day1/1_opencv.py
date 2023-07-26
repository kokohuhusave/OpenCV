import cv2

# ctrl + shift + F10
print("현재 opencv 버전: ",cv2.__version__)

# 컬러영상(BGR), IMREAD_GRAYSCALE: 그레이스케일 영상

img = cv2.imread('./dog.bmp')
cv2.imshow('img', img) # 창이름, 영상
cv2.waitKey() # 키보드 키를 입력전까지 화면이 닫히지 않는다




