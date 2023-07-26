import cv2
import matplotlib.pyplot as plt

'''
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img_gray', img_gray)
cv2.waitKey()
'''

'''
# matplot를 이용한 사진 띄우기
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off') #격자 삭제
plt.imshow(img_gray, cmap='gray')
plt.show()
'''
'''
# cv2.IMREAD_COLOR는 생략 가능(기본값이기 때문에)
img_rgb = cv2.imread('./dog.bmp', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
plt.axis('off') #격자 삭제
plt.imshow(img_rgb)
plt.show() 
'''
'''
# cv2.IMREAD_COLOR는 생략 가능(기본값이기 때문에)
img_rgb = cv2.imread('./dog.bmp', cv2.IMREAD_COLOR)
plt.axis('off') #격자 삭제
plt.imshow(img_rgb)
plt.show() #rgb순서로 인한 결과값
'''
'''
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
img_rgb = cv2.imread('./dog.bmp', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

plt.subplot(121) #1행2열1번째
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(122) #1행2열2번째
plt.axis('off')
plt.imshow(img_rgb)
plt.show()
'''