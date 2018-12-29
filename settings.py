class Settings():
    def __init__(self):
        self.window_width = 400
        self.window_height = 400

        self.chunk_size = 5000
        self.chunks_count = 1

        self.drawing_speed = 1

        self.distance_values  = [4, 8, 16, 32]
        self.distance_weights = [0.8, 0.15, 0.049, 0.001]
        self.distance_vis_threshold = 16