import pygame
from snake.entity import Entity
from math import pi, sin, cos

class SnakeBody(Entity):
    def __init__(self, bound, color=(255, 255, 255), position=(0, 0), size=10):
        self.color = color
        self.size = size
        self.length = 1
        self.body_path = [position]
        self.bound = bound

    def set_color(self, new_color):
        self.color = new_color

    def set_size(self, new_size):
        self.size = size

    def set_position(self, new_position):
        self.position = new_position

    def move(self, direction, speed):
        (last_x, last_y) = self.get_head()
        x = last_x + speed * cos(direction / 180 * pi)
        y = last_y + speed * sin(direction / 180 * pi)
        self.body_path.append((x % self.bound[0], y % self.bound[1]))

        current_len = len(self.body_path)
        if current_len > self.length:
            self.body_path = self.body_path[current_len - self.length:]

    def add_length(self, delta):
        self.length += delta

    def get_head(self):
        return self.body_path[-1]

    def update(self, delta, params):
        pass

    def render(self, screen):
        for p in self.body_path:
            int_position = (int(p[0]), int(p[1]))
            pygame.draw.circle(screen, self.color, int_position, self.size, 0)

