import cv2

img = cv2.imread('./dog.bmp')
cv2.imshow('image', img)

while True:
    keyvalue = cv2.waitKey()
    if keyvalue == ord('i') or keyvalue == ord('I'): # ord 아스키 코드 리턴
        img = ~img
        cv2.imshow('image', img)
    elif keyvalue == 27:
        break

