# 영상모드

import cv2

cap = cv2.VideoCapture('./image/tiger.mp4')

isKeypress = 0  # 0: 일반 영상, 1: 가우시안 필터 영상, 2: 케니 필터 영상

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if isKeypress == 1:
        # 가우시안 필터 적용
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
    elif isKeypress == 2:
        # 케니 필터 적용
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.Canny(frame, 100, 200)

    cv2.imshow('Tiger Video', frame)
    key = cv2.waitKey(10)

    if key == ord(' '):
        isKeypress = (isKeypress + 1) % 3
    elif key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
