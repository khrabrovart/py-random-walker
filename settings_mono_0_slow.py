"""Settings module"""

class Settings():
    def __init__(self):
        self.window_width = 800
        self.window_height = 800

        self.chunk_size = 1500
        self.chunks_count = 100

        self.drawing_speed = 1
        self.drawing_fps = 500

        self.distance_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        self.distance_weights = [0, .2, .6, .2, 0, 0, 0, 0, 0, 0, 0]
        self.distance_vis_threshold = 32
