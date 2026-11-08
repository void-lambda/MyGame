import math

class Entity():
    def __init__(self, x, y, w, h, scale, speed):
        # Moving on maps
        self.x = float(x)
        self.y = float(y)

        # Moving's Vector
        self.dx = 0.0
        self.dy = 0.0

        # Speed
        self.speed = speed  # px/s

        # Literal Width and Height
        self.w = w
        self.h = h

        # Scale normalization
        self.scale = scale

        # Canvas
        self.canvas_id = None

    def set_direction(self, dx, dy):
        """Setting the new location by the difference of X and Y"""
        lenght = math.sqrt(dx * dx * dy * dy)
        if lenght > 0:
            self.dx = dx / lenght
            self.dy = dy / lenght
        else:
            self.dx = dx
            self.dy = dy

    