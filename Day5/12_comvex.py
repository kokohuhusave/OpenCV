import cv2

img = cv2.imread('./hand.jpg')
cpy = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thr = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contous, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contous[0])
cnt = contous[0]
cv2.drawContours(img, [cnt], -1, (255, 0, 0), 2)
check = cv2.isContourConvex(cnt)
print(check) #올록한 부분의 유무 확인

if not check:
    hull = cv2.convexHull(cnt)
    cv2.drawContours(cpy, [hull], -1, (0, 255, 0), 2)
    cv2.imshow('hull', cpy)
cv2.imshow('contour', img)
cv2.waitKey()