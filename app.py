import cv2
import numpy as np

from settings import Settings
from random_walk import RandomWalk

s = Settings()
img = np.zeros((s.window_height, s.window_width, 3), np.uint8)

for chunk_index in range(s.chunks_count):
    rw = RandomWalk(s)
    rw.fill(s)

    red = np.random.randint(0, 128)
    green = np.random.randint(0, 64)
    blue = np.random.randint(160, 256)

    for i, (x, y) in enumerate(zip(rw.xv, rw.yv)):
        if (len(rw.xv) == i + 1):
            break

        if rw.cv[i + 1]:
            cv2.line(img, (rw.xv[i], rw.yv[i]), (rw.xv[i+1], rw.yv[i+1]), (blue, green, red), 1)

        cv2.imshow("Frame", img)

        if i % s.drawing_speed == 0:
            cv2.waitKey(int(1000 / s.drawing_fps))        

print("Complete!")
cv2.waitKey(0) 
cv2.destroyAllWindows()