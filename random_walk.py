"""Main functional module"""

from random import choice
import numpy
import math

class RandomWalk():
    """Random walk class"""

    def __init__(self, s, start_x, start_y):
        self.xv = [int(start_x)]
        self.yv = [int(start_y)]
        self.cv = [False]

    def check_step(self, x, y, s):
        center_x = s.window_width / 2
        center_y = s.window_height / 2

        r = 150
        c1_x = center_x - (r - 20)
        c2_x = center_x + (r - 20)

        in_c1 = (x - c1_x)**2 + (y - (center_y - 100))**2 <= r**2
        in_c2 = (x - c2_x)**2 + (y - (center_y - 100))**2 <= r**2

        in_circles = (in_c1 or in_c2) and y <= center_y
        in_lines = y >= center_y and x + 340 - (y + 100) >= 0 and s.window_width - x + 340 - (y + 100) >= 0
        in_rect = y >= center_y - 100 and y < center_y and abs(x - center_x) < 50

        return in_circles or in_lines or in_rect

    def fill(self, s):
        while len(self.xv) <= s.chunk_size:
            direction = choice([0, 1, 2, 3])
            distance = numpy.random.choice(s.distance_values, p = s.distance_weights)

            x = self.xv[-1]
            y = self.yv[-1]

            if direction == 0:
                y += distance
            elif direction == 1:
                y -= distance
            elif direction == 2:
                x += distance
            elif direction == 3:
                x -= distance

            if self.check_step(x, y, s):
                if len(self.xv) % 5000 == 0: 
                    print("Filled: " + str(len(self.xv)))
                self.xv.append(x)
                self.yv.append(y)
                self.cv.append(distance <= s.distance_vis_threshold)
