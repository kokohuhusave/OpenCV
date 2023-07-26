import cv2
import sys

cap1 = cv2.VideoCapture('./jellyfish_1.mp4')
cap2 = cv2.VideoCapture('./jellyfish_2.mp4')



ret1, frame1 = cap2.read()
while True:
    ret, frame = cap1.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

while True:
    ret1, frame1 = cap2.read()
    if not ret1:
        break
    cv2.imshow('frame', frame1)
    if cv2.waitKey(10) == 27:
        break