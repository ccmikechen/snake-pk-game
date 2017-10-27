import pygame
from snake.entity import Entity

class Food(Entity):
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.generating = True
        self.generating_progress = 0.0

    def active(self, snake):
        snake.add_length(3)

    def update(self, delta):
        if self.generating:
            self.generating_progress += delta

            if self.generating_progress >= 0.5:
                self.generating = False

    def render(self, screen):
        if self.generating:
            size = int(self.generating_progress * self.size * 2)
            pygame.draw.circle(screen, (0, 255, 0), self.position, size, 0)
        else:
            pygame.draw.circle(screen, (0, 255, 0), self.position, self.size, 0)

