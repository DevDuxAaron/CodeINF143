import cv2
import matplotlib.pyplot as plt
imagen = cv2.imread('car_original.jpg', 0)
# plt.imshow(imagen, cmap='gray')
# plt.imshow(imagen[150:300, 400:500], cmap='gray')

img_nueva = cv2.resize(imagen, (1280, 848), interpolation=cv2.INTER_CUBIC)
plt.imshow(img_nueva, cmap='gray')
# plt.imshow(img_nueva[300:600, 800:1000], cmap='gray')
plt.show()