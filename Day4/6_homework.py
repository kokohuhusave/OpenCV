import cv2
import numpy as np

img = cv2.imread('./namecard.jpg')

x=14; y=12; w=730; h=980
roi = img[y:y+h, x:x+w]

cv2.circle(img, (14, 13), 10, (255, 255, 0), -1)
cv2.circle(img, (14, 990), 10, (255, 255, 0), -1)
cv2.circle(img, (740, 13), 10, (255, 255, 0), -1)
cv2.circle(img, (740, 990), 10, (255, 255, 0), -1)

print(roi.shape)
cv2.rectangle(roi, (0,0), (w,h), (0,255,0), 3)
cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()

