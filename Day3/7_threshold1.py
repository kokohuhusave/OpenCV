import cv2
import matplotlib.pyplot as plt

# 이미지 불러오기
src = cv2.imread('./cells.png', cv2.IMREAD_GRAYSCALE)

# 히스토그램 계산
hist = cv2.calcHist([src], [0], None, [256], [0, 255])

# 이진화 수행
a, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
b, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)

# 이미지 표시
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.title('src')
plt.imshow(src, cmap='gray')
plt.axis('off')

plt.subplot(132)
plt.title('dst1 - Threshold: {}'.format(a))
plt.imshow(dst1, cmap='gray')
plt.axis('off')

plt.subplot(133)
plt.title('dst2 - Threshold: {}'.format(b))
plt.imshow(dst2, cmap='gray')
plt.axis('off')

plt.show()

# 히스토그램 표시
plt.figure()
plt.title('Histogram')
plt.plot(hist)
plt.show()

# 밝은 사진이다 보니 오른쪽에 치우쳐져있는것을 알수있다