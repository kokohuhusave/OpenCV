import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = cv2.imread('./namecard.jpg')

w, h = 600, 400

srcQuad = np.array([[186, 204], [892, 202], [930, 570], [170, 580]], np.float32)
# 좌표
dstQuad = np.array([[0, 0], [w, 0], [w, h], [0, h]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(img, pers, (w, h))


cv2.imshow('dst', dst)


dst1 = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(dst1, lang='kor+eng') #영어랑 한글도 감안해서 읽는다
print(text)

cv2.waitKey()