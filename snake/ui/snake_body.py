import pygame
from snake.entity import Entity
from math import pi, sin, cos, atan2, sqrt

def to_int_position(pos):
    return (int(pos[0]), int(pos[1]))

def calc_distance(pos_a, pos_b):
    return sqrt((pos_a[0] - pos_b[0])**2 + (pos_a[1] - pos_b[1])**2)

def draw_rounded_line(surface, color, start_pos, end_pos, width):
    angle = atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0]) / pi * 180
    current_pos = next_pos(start_pos, width, angle)
    end_pos = to_int_position(end_pos)

    while calc_distance(current_pos, end_pos) > width:
        pygame.draw.circle(surface, color, current_pos, width, 0)
        current_pos = next_pos(current_pos, width, angle)

    pygame.draw.circle(surface, color, end_pos, width, 0)

def next_pos(start_pos, length, angle):
    x = start_pos[0] + length * cos(angle / 180 * pi)
    y = start_pos[1] + length * sin(angle / 180 * pi)

    return to_int_position((x, y))

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
#        start_pos = self.body_path[0]

        for pos in self.body_path:
            pygame.draw.circle(screen, self.color, to_int_position(pos), self.size, 0)
#            draw_rounded_line(screen, self.color, start_pos, pos, self.size)

