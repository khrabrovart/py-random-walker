import numpy

from settings import Settings
from random import choice

class RandomWalk():
    def __init__(self, s):
        self.xv = [numpy.random.randint(0, s.window_width)]
        self.yv = [numpy.random.randint(0, s.window_height)]
        self.cv = [False]

    def fill(self, s):
        last_step_direction = 0

        while len(self.xv) < s.chunk_size:
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

            if x >= 0 and x <= s.window_width and y >= 0 and y <= s.window_height:
                self.xv.append(x)
                self.yv.append(y)
                self.cv.append(distance <= s.distance_vis_threshold)

                last_step_direction = direction