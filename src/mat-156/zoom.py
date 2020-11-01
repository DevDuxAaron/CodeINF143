import cv2
import matplotlib.pyplot as plt
# 1 Leer la imagen
bgr = cv2.imread("full_car.jpg")
# 2 Convertir a rgb
rgb = bgr[..., ::-1].copy()
# 3 Extraer un pedazo
work = rgb[1450:1645, 350:600]
# 4 Canal de cada color
b, g, r = cv2.split(work)
# 5 Aplicando interpolacion
img_nueva_r = cv2.resize(r, (500, 390), interpolation=cv2.INTER_CUBIC)
img_nueva_g = cv2.resize(g, (500, 390), interpolation=cv2.INTER_CUBIC)
img_nueva_b = cv2.resize(b, (500, 390), interpolation=cv2.INTER_CUBIC)
# 6 Uniendo de nuevo
new_rgb = cv2.merge((img_nueva_r, img_nueva_g, img_nueva_b))
# 7 de rgb a bgr
new_img_bgr = new_rgb[..., ::-1].copy()
# 8 Guardando el archivo nuevo
cv2.imwrite('imagen_result.jpg', new_img_bgr)

# Comparando con resize
new_resized = cv2.resize(rgb[1450:1645, 350:600], (500, 390))

# Nueva imagen obtenida
# plt.imshow(new_img_bgr)

# Imagen original
plt.imshow(new_resized)
plt.show()
