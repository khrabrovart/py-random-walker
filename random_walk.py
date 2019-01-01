"""Main functional module"""

from random import choice
import numpy

class RandomWalk():
    """Random walk class"""

    def __init__(self, s):
        start_x = numpy.random.randint(0, s.window_width)
        start_y = numpy.random.randint(0, s.window_height)

        start_x_shift = start_x % s.chunk_offset
        if start_x_shift != 0:
            start_x += s.chunk_offset - start_x_shift

        start_y_shift = start_y % s.chunk_offset
        if start_y_shift != 0:
            start_y += s.chunk_offset - start_y_shift

        self.xv = [start_x]
        self.yv = [start_y]
        self.cv = [False]

    def fill(self, s):
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
