import numpy as np
from numba import jit
from scipy.fftpack import dct, idct
import cv2
import matplotlib.pyplot as plt
import pickle

@jit(nopython=True)
def alpha(u: int, n: int):
    return np.sqrt(1/n) if u == 0 else np.sqrt(2/n)

@jit(nopython=True)
def r(x: int, y: int, u: int, v: int, n: int, m: int):
    return alpha(u,n)*alpha(v,m)*np.cos(((2*x+1)*u*np.pi)/(2*n))*np.cos(((2*y+1)*v*np.pi)/(2*m))


@jit(nopython=True)
def transform(u: int, v: int, mat: np.ndarray):
    t = 0
    n, m = mat.shape

    for y in range(n):
        for x in range(m):
            t += mat[y, x] * r(x, y, u, v, n, m)

    return t


@jit(nopython=True)
def mdct(patch: np.ndarray):
    res = np.zeros((8, 8)).astype(np.int16)
    n = res.shape[0]

    for v in range(n):
        for u in range(n):
            res[v, u] = transform(u, v, patch)

    return res


coeff = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

matrix = np.ones((8, 8), dtype=np.int32)*255
res = mdct(matrix)

print(res)

def mat_dct(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


mat_dct(matrix)


@jit(nopython=True)
def itransform(x: int, y: int, mat: np.ndarray):
    t = 0
    n, m = mat.shape

    for v in range(n):
        for u in range(m):
            t += mat[v, u] * r(x, y, u, v, n, m)

    return t


@jit(nopython=True)
def midct(patch: np.ndarray, shape):
    res = np.zeros(shape).astype(np.int16)
    n, m = res.shape

    for y in range(n):
        for x in range(m):
            res[y, x] = itransform(x, y, patch)

    return res


midct(res, (8, 8))

# array([[255, 255, 255, 255, 255, 255, 255, 255],
#        [255, 255, 255, 255, 255, 255, 255, 255],
#        [255, 255, 255, 255, 255, 255, 255, 255],
#        [255, 255, 255, 255, 255, 255, 255, 255],
#        [255, 255, 255, 255, 255, 255, 255, 255],
#        [255, 255, 255, 255, 255, 255, 255, 255],
#        [255, 255, 255, 255, 255, 255, 255, 255],
#        [255, 255, 255, 255, 255, 255, 255, 255]], dtype=int16)

# Comprimir



# plt.imshow(img, cmap='gray')
# plt.show()


@jit(nopython=True)
def compress(img: np.ndarray, coeficients: np.ndarray):
    res = []
    for i in range(0, img.shape[0], 8):
        for j in range(0, img.shape[1], 8):
            block = img[i:i + 8, j:j + 8]
            block_dct = mdct(block)

            res.append(block_dct[0, 0] // coeficients[0, 0])
            res.append(block_dct[0, 1] // coeficients[0, 1])
            res.append(block_dct[1, 0] // coeficients[1, 0])
            res.append(block_dct[2, 0] // coeficients[2, 0])
            res.append(block_dct[1, 1] // coeficients[1, 1])
            res.append(block_dct[0, 2] // coeficients[0, 2])

    return np.array(res, dtype=np.int32)


img = cv2.imread('Original.png', 0)

compressed = compress(img, coeff)
compressed_full = (img.shape, compressed)
with open('c.dat', 'wb') as file:
    pickle.dump(compressed_full, file)


@jit(nopython=True)
def decompress(compressed_data, coeficients):
    shape, data = compressed_data
    res = np.zeros(shape).astype(np.int16)

    k = 0
    for i in range(0, shape[0], 8):
        for j in range(0, shape[1], 8):
            patch = data[k:k + 6]

            block_shape = res[i:i + 8, j:j + 8].shape
            block = np.zeros(block_shape[0] * block_shape[1])

            block = block.reshape(block_shape)
            block[0, 0] = patch[0] * coeficients[0, 0]
            block[0, 1] = patch[1] * coeficients[0, 1]
            block[1, 0] = patch[2] * coeficients[1, 0]
            block[2, 0] = patch[3] * coeficients[2, 0]
            block[1, 1] = patch[4] * coeficients[1, 1]
            block[0, 2] = patch[5] * coeficients[0, 2]

            block_idct = midct(block, block_shape)

            res[i:i + 8, j:j + 8] = block_idct
            k += 6

    return res.astype(np.uint8)


decompressed = decompress(compressed_full, coeff)