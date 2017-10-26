import pygame, sys
import random
from sprite_sheet import SpriteSheet

class Fire(SpriteSheet):
    def __init__(self):
        super().__init__('./images/fire.png', (512/8, 512/4))
        self.animation_counter = random.randint(0, 15)

    def animate(self, screen, x, y):
        image_x = int(self.animation_counter / 8)
        image_y = int(self.animation_counter % 4)
        print(image_x, image_y)
        image = self.image_at(image_x, image_y)
        self.animation_counter = (self.animation_counter + 1) % (8 * 4)

        screen.blit(image, (x, y))
