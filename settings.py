class Settings():
    def __init__(self):
        self.window_width = 800
        self.window_height = 800

        self.chunk_size = 7000
        self.chunks_count = 100
        self.chunk_offset = 8

        self.drawing_speed = 100
        self.drawing_fps = 1000

        self.distance_values  = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        self.distance_weights = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.distance_vis_threshold = 32