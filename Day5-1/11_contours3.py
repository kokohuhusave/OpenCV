# 근사화 정밀도 조절에서 if문을 이용하여 사진 속 도형들의 Label 이름 넣기

import cv2

def get_shape_label(num_sides):
    if num_sides == 3:
        return 'Triangle'
    elif num_sides == 4:
        return 'Rectangle'
    elif num_sides == 5:
        return 'Pentagon'
    elif num_sides == 6:
        return 'Hexagon'
    else:
        return 'Unknown'

img = cv2.imread('./image/polygon.bmp', cv2.IMREAD_GRAYSCALE)
_, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    num_sides = len(approx)
    if num_sides >= 3:
        shape_label = get_shape_label(num_sides)

        moment = cv2.moments(contour)
        cx = int(moment["m10"] / moment["m00"])
        cy = int(moment["m01"] / moment["m00"])

        cv2.putText(img, shape_label, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

cv2.imshow('labeled_img', img)
cv2.waitKey()