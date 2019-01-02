"""App module"""

import cv2
import numpy as np
from random_walk import RandomWalk

from settings_mono_release import Settings

def run_visualization():
    """Main visualization method"""

    s = Settings()
    img = np.zeros((s.window_height, s.window_width, 3), np.uint8)

    shape_start_x = s.window_width / 2
    shape_start_y = s.window_height / 2

    bg_start_x = 0
    bg_start_y = 0

    for chunk_index in range(s.chunks_count):
        shape_walker = RandomWalk(s, shape_start_x, shape_start_y)
        shape_walker.fill(s, True)

        bg_walker = RandomWalk(s, bg_start_x, bg_start_y)
        bg_walker.fill(s, False)

        shape_red = np.random.randint(150, 200)
        shape_green = np.random.randint(0, 64)
        shape_blue = np.random.randint(150, 200)

        bg_red = np.random.randint(0, 1)
        bg_green = np.random.randint(0, 1)
        bg_blue = int(np.random.choice([0, 60, 70, 80, 90, 100], p=[.4, .3, .1, .1, .05, .05]))

        for i, val in enumerate(shape_walker.xv):
            if len(shape_walker.xv) == i + 1:
                break

            if shape_walker.cv[i + 1]:
                cv2.line(img, (shape_walker.xv[i], shape_walker.yv[i]), (shape_walker.xv[i+1], shape_walker.yv[i+1]), (shape_blue, shape_green, shape_red), 1)

            cv2.line(img, (bg_walker.xv[i], bg_walker.yv[i]), (bg_walker.xv[i+1], bg_walker.yv[i+1]), (bg_blue, bg_green, bg_red), 1)

            cv2.imshow("Frame", img)

            if i % s.drawing_speed == 0:
                cv2.waitKey(int(1000 / s.drawing_fps))  

        shape_start_x = shape_walker.xv[-1]
        shape_start_y = shape_walker.yv[-1]

        bg_start_x = bg_walker.xv[-1]
        bg_start_y = bg_walker.yv[-1]

    print("Complete!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

run_visualization()
