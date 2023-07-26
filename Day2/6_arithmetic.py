import cv2
import matplotlib.pyplot as plt


src1 = cv2.imread('./square.bmp')  # replace with your image path
src2 = cv2.imread('./flowers.jpg')  # replace with your image path


src2_resized = cv2.resize(src2, (src1.shape[1], src1.shape[0]))


dst_add = cv2.add(src1, src2_resized)
dst_addWeighted = cv2.addWeighted(src1, 0.5, src2_resized, 0.5, 0)
dst_subtract = cv2.subtract(src1, src2_resized)
dst_absdiff = cv2.absdiff(src1, src2_resized)

img = {'src1': src1, 'src2_resized': src2_resized, 'dst_add': dst_add, 'dst_addWeighted': dst_addWeighted, 'dst_subtract': dst_subtract, 'dst_absdiff': dst_absdiff}

# Plotting
plt.figure(figsize=(12, 12))
for i, (k, v) in enumerate(img.items()):
    plt.subplot(3, 2, i+1)
    plt.imshow(cv2.cvtColor(v, cv2.COLOR_BGR2RGB))  # Convert the image color from BGR to RGB
    plt.title(k)
plt.show()
