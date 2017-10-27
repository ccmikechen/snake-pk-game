from snake.entity import Entity
from snake.ui.snake_body import SnakeBody

class Snake(Entity):
    def __init__(self, bound, position):
        self.direction = 90
        self.speed = 100
        self.body = SnakeBody(bound, position=position)

    def set_position(self, position):
        self.body.set_position(position)

    def set_speed(self, speed):
        self.speed = speed

    def set_direction(self, direction):
        self.direction = direction

    def add_direction(self, delta):
        self.direction = (self.direction + delta + 360) % 360

    def set_color(self, color):
        self.body.set_color(color)

    def add_length(self, delta):
        self.body.add_length(delta)

    def update(self, delta):
        self.body.move(self.direction, self.speed * delta)

    def render(self, screen):
        self.body.render(screen)

