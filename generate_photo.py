import cv2
import numpy as np
import random
img = np.zeros([625, 25, 3])
print(img.shape)
for i in range(625):
    for j in range(25):
        x = random.randint(0, 63) 
        y = random.randint(0, 63)
        z = random.randint(0, 1)
        img[i, j, 0] = x
        img[i, j, 1] = y
        img[i, j, 2] = z
cv2.imwrite('mapindex.png', img)