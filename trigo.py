import math
PI = math.pi

class Trigonometry:
    def __init__(self):
        self.co_ordinates = []

    def sin(self):
        for x in range(-800, 800):
            y = math.sin(x/78)
            x_y = (x, y*105)
            self.co_ordinates.append(x_y)

    def cos(self):
        for x in range(-800, 800):
            x = x/314
            y = math.cos(x/78)
            x_y = (x, y*105)
            self.co_ordinates.append(x_y)
