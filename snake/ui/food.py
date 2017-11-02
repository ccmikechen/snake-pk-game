import pygame
from snake.resource import R
from snake.entity import Entity

class Food(Entity):
    def __init__(self, position, size, color=(0, 255, 0)):
        self.position = position
        self.size = size
        self.color = color
        self.generating = True
        self.generating_progress = 0.0

    def active(self, snake):
        R.get_sound("eat").play()
        snake.add_length(10)

    def update(self, delta):
        if self.generating:
            self.generating_progress += delta

            if self.generating_progress >= 0.2:
                self.generating = False

    def render(self, screen):
        if self.generating:
            size = int(self.generating_progress * self.size * 5)
            pygame.draw.circle(screen, self.color, self.position, size, 0)
        else:
#            food_image = pygame.transform.scale(R.get_image("blood"), (self.size, self.size))
#            screen.blit(food_image, self.position)

            pygame.draw.circle(screen, self.color, self.position, self.size, 0)

