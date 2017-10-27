from snake.ui.snake_body import SnakeBody
from math import pi, sin, cos

DEFAULT_COLOR = (255, 255, 255)

class SnakeHead(SnakeBody):
    def move(self, direction, speed):
        x = self.position[0] + speed * cos(direction / 180 * pi)
        y = self.position[1] + speed * sin(direction / 180 * pi)
        super().move(x, y)
