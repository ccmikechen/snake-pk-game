from snake.entity import Entity
from snake.ui.snake_body import SnakeBody
from math import sqrt

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

    def get_length(self):
        return self.body.length

    def get_head(self):
        return self.body.get_head()

    def count_collisions(self, snakes):
        counter = 0
        head = self.body.get_head()

        for snake in snakes:
            snake_body = snake.body
            for body in snake_body.body_path:
                if self._check_collision(head, self.body.size, body, snake_body.size):
                    counter += 1

        return counter

    def update(self, delta):
        self.body.move(self.direction, self.speed * delta)

    def render(self, screen):
        self.body.render(screen)

    def _check_collision(self, pos_a, size_a, pos_b, size_b):
        distance = sqrt((pos_a[0] - pos_b[0])**2 + (pos_a[1] - pos_b[1])**2)
        return distance <= (size_a + size_b)
