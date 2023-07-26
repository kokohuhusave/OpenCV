import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the images
src1 = cv2.imread('./flowers.jpg')
src2 = cv2.imread('./pink.jpg')

# Resize 'src2' to match the shape of 'src1'
src2_resized = cv2.resize(src2, (src1.shape[1], src1.shape[0]))

alpha = 0.7

dst1 = src1 * alpha + src2_resized * (1-alpha)
dst1 = dst1.astype(np.uint8)

dst2 = cv2.addWeighted(src1, alpha, src2_resized, (1-alpha), 0)

img = {'src1': src1, 'src2_resized': src2_resized, 'dst1': dst1, 'dst2': dst2}

# Display the images
for key in img:
    cv2.imshow(key, img[key])
cv2.waitKey(0)
cv2.destroyAllWindows()
