import cv2
import matplotlib.pyplot as plt

# Load the images
src1 = cv2.imread('./flowers.jpg')
src2 = cv2.imread('./pink.jpg')


src2_resized = cv2.resize(src2, (src1.shape[1], src1.shape[0]))


dst1 = src1 + src2_resized
dst2 = cv2.add(src1, src2_resized)

img = {'src1': src1, 'src2_resized': src2_resized, 'dst1': dst1, 'dst2': dst2}

# Plotting
plt.figure(figsize=(10, 10))
for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(cv2.cvtColor(v, cv2.COLOR_BGR2RGB))  # Convert the image color from BGR to RGB
    plt.title(k)
plt.show()
