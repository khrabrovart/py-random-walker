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

    def check_step_in_shape(self, x, y, s):
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

    def check_step_in_bg(self, x, y, s):
        return not self.check_step_in_shape(x, y, s) and x >= 0 and x <= s.window_width and y >= 0 and y <= s.window_height

    def fill(self, s, is_shape):
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

            if is_shape:
                if self.check_step_in_shape(x, y, s):
                    self.xv.append(x)
                    self.yv.append(y)
                    self.cv.append(distance <= s.distance_vis_threshold)
            elif self.check_step_in_bg(x, y, s):
                self.xv.append(x)
                self.yv.append(y)
                self.cv.append(True)