import cv2

img = cv2.imread('./sun.jpg')

x, y, w, h = cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi', roi)
#엔터키 클릭시 영역 자름
cv2.waitKey()

